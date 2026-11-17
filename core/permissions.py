from rest_framework.permissions import BasePermission


class IsSuperuserAndStaff(BasePermission):
    """Acesso restrito a contas ativas com is_superuser e is_staff juntos."""

    def has_permission(self, request, view):
        user = request.user
        return bool(
            user
            and user.is_authenticated
            and getattr(user, "is_active", False)
            and getattr(user, "is_superuser", False)
            and getattr(user, "is_staff", False)
        )
