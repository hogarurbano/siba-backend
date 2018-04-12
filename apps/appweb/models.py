from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=65)
    comments = models.CharField(max_length=65)

    l_TypeID = (('0', 'RUT'), ('1', 'NIT'))
    type = models.CharField(max_length=1, choices=l_TypeID, default='0')

    idcode = models.CharField(max_length=50)

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey('auth.User', related_name='company_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='company_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

    def accountname(self):
        s_value = "{0} ({1})"
        return s_value.format(self.name, self.idcode)

    def __str__(self):
        return self.accountname()

class country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    code= models.CharField(max_length=6)

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey('auth.User', related_name='country', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='country_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

class account_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='acctype_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='acctype_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

    def account_type(self):
        s_value = "{0} ({1})"
        return s_value.format(self.name, self.id)

    def __str__(self):
        return self.account_type()

class country(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='country_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='country_modifiers', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')

    def __str__(self):
        return self.name

class city(models.Model):
    name = models.CharField(verbose_name=_('City name'), max_length=255)
    country = models.ForeignKey(country, verbose_name=_('Country'), related_name='city_country', on_delete=models.CASCADE, null=True)
    code = models.IntegerField(verbose_name=_('City Code'))

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='city_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='city_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        unique_together = ('name', 'country')

    def __str__(self):
        return self.name


class address(models.Model):
    name = models.CharField(verbose_name=_('Address'), max_length=255)
    city = models.ForeignKey(city, verbose_name=_('city'), related_name='addresses_city', on_delete=models.CASCADE)
    zip = models.IntegerField(_('zip/postal code'))

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='address_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='address_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')
        unique_together = ('name', 'city')

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return 'name', 'city__name'

class account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=65)
    slug = models.SlugField(null=True)
    accountnumber = models.CharField(max_length=50)
    address = models.CharField(max_length=30, default='')
    addressnumber = models.CharField(max_length=6, default=0)
    city = models.CharField(max_length=65, null=False, default='')
    state = models.CharField(max_length=30, null=False, default='')
    country = models.CharField(max_length=65, default='CHILE', null=True)

    type = models.ForeignKey(account_type, on_delete=True )
    company = models.ForeignKey(company,on_delete=models.CASCADE,related_name='acc_company',parent_link=True, null=True)

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='account_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='account_modifiers', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
        unique_together = ('name', 'accountnumber')

    def __str__(self):
        return self.name

class contact(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    identification = models.CharField(max_length=35)
    phone = models.CharField(max_length=35)
    state = models.BooleanField(default=True)
    account = models.OneToOneField(account, on_delete=models.SET_NULL, null=True)

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='contact_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='contact_modifiers', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        unique_together = ('firstname', 'lastname')

    def contactname(self):
        s_value = "{0} {1}"
        return s_value.format(self.firstname, self.lastname)

    def __str__(self):
        return self.contactname()

class UserProfile(models.Model):
    url = models.URLField("Website", blank=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    company = models.OneToOneField(company, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user()
