from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MainConfig(AppConfig):
    name = 'physhik.blog'
    verbose_name = _("Blog")

    def ready(self):
        try:
            pass
        except ImportError:
            pass