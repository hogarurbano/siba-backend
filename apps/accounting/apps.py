from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SibaAccountingConfig(AppConfig):
    name = 'apps.accounting'
    verbose_name = _("Accounting")
