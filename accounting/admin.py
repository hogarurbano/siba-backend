from .models import *
from accounting import forms
from django.utils.translation import ugettext_lazy as _

# Register Transaction Object
class BankAdmin(admin.ModelAdmin):
    form = forms.BankAcctForm

    list_display = ('bankname', 'accountlabel', 'accountnumber', 'accountcurrency', 'createdby')
    readonly_fields = ('lastmodifieddate', 'lastmodifiedby',)
    fieldsets = (
        (
            None, {
                'fields': ('accountreference', 'accountlabel', 'companyid', 'bankname', 'bankcode')

                }
        ), (
            _('Information account'), {
                'fields': ('accountnumber','accountcurrency', 'mim_allowed', 'mim_desired'),
                'classes': ('expand',)
            }
        ), (
            _('Contact account'), {
                'fields': ('comments','lastmodifieddate', 'lastmodifiedby'),
                'classes': ('expand',)
            }
        )
    )

    def save_model(self, request, obj, form, change):
        if not obj.createdby:
            obj.createdby = request.user
        obj.lastmodifiedby = request.user
        obj.save()

admin.site.register(bank_account, BankAdmin)

# Register Transaction Object
class TransAdmin(admin.ModelAdmin):
    form = forms.TransForm

    list_display = ('dateoperation', 'datevalue', 'amount', 'bankaccount', 'createdby')
    readonly_fields = ('lastmodifieddate', 'lastmodifiedby',)
    fieldsets = ((
                     None, {
                         'fields': ('transcode', 'dateoperation', 'datevalue', 'amount',
                                    'description','bankaccount', 'owner')
                     }), (
                        _('Otra información'), {
                         'fields': ('note','lastmodifieddate', 'lastmodifiedby'),
                         'classes': ('expand',)
                     })
    )

    def save_model(self, request, obj, form, change):
        if not obj.createdby:
            obj.createdby = request.user
        obj.lastmodifiedby = request.user
        obj.save()

admin.site.register(trans, TransAdmin)