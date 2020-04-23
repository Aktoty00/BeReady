from django.apps import AppConfig


class AuthabConfig(AppConfig):
    name = 'authAB_'

    def ready(self):
        import authAB_.signals
