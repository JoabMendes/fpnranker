from django.apps import AppConfig


class DomainConfig(AppConfig):
    name = 'domain'

    def ready(self):
        # import signal handlers
        from domain.signals import competition_round_pre_save_handler  # noqa
