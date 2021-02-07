from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = 'test_app'

    def ready(self):
        import pydevd_pycharm
        pydevd_pycharm.settrace(
            'host.docker.internal', port=57588, stdoutToServer=True, stderrToServer=True, suspend=False)