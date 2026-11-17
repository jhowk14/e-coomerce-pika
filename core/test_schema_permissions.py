"""Schema e swagger só para conta ativa com is_superuser e is_staff juntos."""

from django.contrib.auth.models import AnonymousUser
from django.test import SimpleTestCase
from django.urls import resolve
from rest_framework.test import APIRequestFactory, force_authenticate
from shared_auth.models import User

from core.permissions import IsSuperuserAndStaff

SCHEMA_ROUTES = ("/api/schema/", "/api/schema/swagger-ui/")


def _user(**flags):
    return User(pk=1, username="conta", **flags)


class IsSuperuserAndStaffTests(SimpleTestCase):
    def _allowed(self, user):
        request = APIRequestFactory().get("/api/schema/")
        request.user = user
        return IsSuperuserAndStaff().has_permission(request, None)

    def test_only_active_superuser_with_staff_passes(self):
        self.assertFalse(self._allowed(None))
        self.assertFalse(self._allowed(AnonymousUser()))
        self.assertFalse(self._allowed(_user()))
        self.assertFalse(self._allowed(_user(is_staff=True)))
        self.assertFalse(self._allowed(_user(is_superuser=True)))
        self.assertFalse(
            self._allowed(_user(is_superuser=True, is_staff=True, is_active=False))
        )
        self.assertTrue(self._allowed(_user(is_superuser=True, is_staff=True)))


class SchemaRoutesPermissionTests(SimpleTestCase):
    def _get(self, path, user=None):
        request = APIRequestFactory().get(path)
        if user is not None:
            force_authenticate(request, user)
        match = resolve(path)
        return match.func(request, *match.args, **match.kwargs)

    def test_routes_use_the_restricted_permission(self):
        for path in SCHEMA_ROUTES:
            with self.subTest(path=path):
                self.assertEqual(
                    resolve(path).func.view_class.permission_classes,
                    [IsSuperuserAndStaff],
                )

    def test_anonymous_is_denied(self):
        for path in SCHEMA_ROUTES:
            with self.subTest(path=path):
                self.assertIn(self._get(path).status_code, (401, 403))

    def test_accounts_without_both_flags_are_denied(self):
        users = {
            "normal": _user(),
            "staff": _user(is_staff=True),
            "superuser": _user(is_superuser=True),
            "inactive": _user(is_superuser=True, is_staff=True, is_active=False),
        }
        for path in SCHEMA_ROUTES:
            for label, user in users.items():
                with self.subTest(path=path, user=label):
                    self.assertEqual(self._get(path, user).status_code, 403)

    def test_superuser_with_staff_is_allowed(self):
        user = _user(is_superuser=True, is_staff=True)
        for path in SCHEMA_ROUTES:
            with self.subTest(path=path):
                self.assertEqual(self._get(path, user).status_code, 200)
