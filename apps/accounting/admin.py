from django.contrib import admin
from .models import *
from apps.accounting import forms
from django.utils.translation import ugettext_lazy as _

admin.site.register(bank_account)

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