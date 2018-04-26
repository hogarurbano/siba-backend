from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SibaConfig(AppConfig):
    name = 'appweb'
    verbose_name = _("Setting SIBA")
