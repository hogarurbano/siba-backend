from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from apps.appweb import forms
from django.utils.translation import ugettext_lazy as _

# Register your models here.

admin.site.register(company)
admin.site.register(contact)
admin.site.register(account_type)
admin.site.register(UserProfile)
admin.site.register(country)

# Register Account Object
class AccountEntryAdmin(admin.ModelAdmin):
    form = forms.AccountEntryForm

    list_display = ('name', 'accountnumber', 'lastmodifieddate', 'createdby')
    prepopulated_fields = {'slug': ['name']}
    readonly_fields = ('lastmodifieddate', 'lastmodifiedby',)
    fieldsets = ((
                     None, {
                         'fields': ('name', 'accountnumber', 'type', 'company',
                                    'address', 'addressnumber', 'city', 'state', 'country',
                                    'createdby')
                     }), (
                        _('Otra información'), {
                         'fields': ('lastmodifieddate', 'lastmodifiedby', 'slug'),
                         'classes': ('expand',)
                     })
    )

    def save_model(self, request, obj, form, change):
        if not obj.createdby.id:
            obj.createdby = request.user
        obj.lastmodifiedby = request.user
        obj.save()

admin.site.register(account, AccountEntryAdmin)

# Register Account Object
class CityAdmin(admin.ModelAdmin):
    form = forms.CityForm

    list_display = ('name', 'country', 'lastmodifieddate', 'createdby')
    readonly_fields = ('lastmodifieddate', 'lastmodifiedby',)
    fieldsets = ((
                     _('General'), {
                         'fields': ('name', 'country')
                     }), (
                        _('Otra información'), {
                         'fields': ('code','lastmodifieddate', 'lastmodifiedby'),
                         'classes': ('expand',)
                     })
    )

    def save_model(self, request, obj, form, change):
        if not obj.createdby:
            obj.createdby = request.user
        obj.lastmodifiedby = request.user
        obj.save()

admin.site.register(city, CityAdmin)