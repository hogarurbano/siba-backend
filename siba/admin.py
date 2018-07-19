from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from . import forms
from django.utils.translation import ugettext_lazy as _

# Register Company Object
class CompanyAdmin(admin.ModelAdmin):
    form = forms.CompanyForm

    list_display = ('name', 'type', 'lastmodifieddate', 'createdby')
    readonly_fields = ('lastmodifieddate', 'lastmodifiedby',)
    fieldsets = ((
                     _('General'), {
                         'fields': ('name', 'type', 'idcode', 'payment_duedays', 'startdate',
                                    'totaltown', 'totalcondominium', 'logo')
                     }), (
                        _('Address Information'), {
                         'fields': ('contactmain', 'phone', 'email',
                                    'address', 'addressnumber', 'city', 'state', 'country',
                                    'url'),
                         'classes': ('expand',)
                     }), (
                        _('Other information'), {
                         'fields': ('comments','lastmodifieddate', 'lastmodifiedby'),
                         'classes': ('expand',)
                     })
    )

    def save_model(self, request, obj, form, change):
        if not obj.createdby:
            obj.createdby = request.user
        obj.lastmodifiedby = request.user
        obj.save()
admin.site.register(company, CompanyAdmin)

class UnitAdmin(admin.ModelAdmin):
    form = forms.UnitForm

    list_display = ('unitnumber', 'aliquot', 'type', 'lastmodifieddate', 'createdby')
    readonly_fields = ('id', 'lastmodifieddate', 'lastmodifiedby',)
    fieldsets = ((
                     None, {
                         'fields': ('unitnumber', 'type', 'company', 'aliquot')
                     }), (
                        _('Other information'), {
                         'fields': ('comments','lastmodifieddate', 'lastmodifiedby'),
                         'classes': ('expand',)
                     })
    )

    def save_model(self, request, obj, form, change):
        if not obj.createdby:
            obj.createdby = request.user
        obj.lastmodifiedby = request.user
        obj.save()

admin.site.register(unit, UnitAdmin)

admin.site.register(contact)

class AccTypeAdmin(admin.ModelAdmin):
    form = forms.AccTypeForm

    list_display = ('name', 'lastmodifieddate', 'createdby')
    readonly_fields = ('lastmodifieddate', 'lastmodifiedby',)
    fields = ('name', 'lastmodifieddate', 'lastmodifiedby')

    def save_model(self, request, obj, form, change):
        if not obj.createdby:
            obj.createdby = request.user
        obj.lastmodifiedby = request.user
        obj.save()

admin.site.register(account_type, AccTypeAdmin)

admin.site.register(UserProfile)

# Register Account Object
class AccountAdmin(admin.ModelAdmin):
    form = forms.AccountForm

    list_display = ('name', 'accountnumber', 'type', 'company', 'lastmodifieddate', 'createdby')
    readonly_fields = ('lastmodifieddate', 'lastmodifiedby',)
    fieldsets = ((
                     None, {
                         'fields': ('name', 'accountnumber', 'type', 'company', 'aliquot',
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

admin.site.register(account, AccountAdmin)

# Register Country and City Objects

class CityInLine(admin.TabularInline):
    model = city
    extra = 1

class CountryAdmin(admin.ModelAdmin):
    fieldsets = [(
                     None, {
                         'fields': ('name', 'code')
                     }), (
                     _('Otra información'), {
                         'fields': ('lastmodifieddate', 'lastmodifiedby'),
                         'classes': ('expand',)
                     })
    ]
    readonly_fields = ('lastmodifieddate', 'lastmodifiedby',)
    search_fields = ['name']
    inlines = [CityInLine]
    list_display = ('name', 'code', 'lastmodifieddate', 'createdby')
    list_per_page = 10
    list_filter = ['name', 'lastmodifieddate']




    def save_model(self, request, obj, form, change):
        if not obj.createdby:
            obj.createdby = request.user
        obj.lastmodifiedby = request.user
        obj.save()

admin.site.register(country, CountryAdmin)