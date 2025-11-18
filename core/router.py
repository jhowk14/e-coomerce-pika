from shared_auth.router import SharedAuthRouter

class CoreRouter(SharedAuthRouter):
    route_app_labels = {"shared_auth", "auth", "admin", "contenttypes"}