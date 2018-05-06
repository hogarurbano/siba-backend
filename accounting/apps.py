from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class SIBAAccountingConfig(AppConfig):
    name = 'accounting'
    verbose_name = _("SIBA Accounting")