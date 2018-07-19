from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, db_index=True, max_length=65, verbose_name=_('Company Name'))
    comments = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, verbose_name=_('Logo'))

    l_TypeID = (('0', 'RUT'), ('1', 'NIT'))
    type = models.CharField(max_length=1, choices=l_TypeID, default='0', verbose_name=_('Ref type'))
    idcode = models.CharField(max_length=50, db_index=True, verbose_name=_('Ref number'))
    startdate = models.DateField(null=True)
    payment_duedays = models.IntegerField(default=0, verbose_name=_('Payment due days'))

    address = models.CharField(max_length=30, verbose_name=_('Address'), default='')
    AddressNumber = models.CharField(max_length=6, verbose_name=_('Address number'), default=0)
    city = models.CharField(max_length=65, null=False, default='', verbose_name=_('City'))
    state = models.CharField(max_length=30, null=False, default='', verbose_name=_('State'))
    country = models.CharField(max_length=65, default='CHILE', null=True, verbose_name=_('Country'))

    totaltown = models.IntegerField(default=0, verbose_name=_('Total number Town'))
    totalcondominium = models.IntegerField(default=0, verbose_name=_('Total number Condominiums'))

    contactmain = models.CharField(max_length=45, null=True, verbose_name=_('Contact main'))
    email = models.EmailField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=_(
                                     "Phone number must be entered in the format: '+999123456789'. Up to 15 digits allowed."))
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    url = models.URLField(null=True, blank=True, verbose_name=_('Url page'))

    createddate = models.DateTimeField(default=timezone.now, verbose_name=_('Created Date'))
    createdby = models.ForeignKey(User, related_name='company_user', verbose_name=_('Created by'),
                                  on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True, verbose_name=_('Modified date'))
    lastmodifiedby = models.ForeignKey(User, related_name='company_modifiers', verbose_name=_('Modified by'),
                                       on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def df_companyname(self):
        s_value = "{0} - {1}"
        return s_value.format(self.idcode, self.name)

    def __str__(self):
        return self.df_companyname()


class account_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    createddate = models.DateTimeField(default=timezone.now, verbose_name=_('Created date'))
    createdby = models.ForeignKey(User, related_name='acctype_user', verbose_name=_('Created by'),
                                  on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True, verbose_name=_('Modified date'))
    lastmodifiedby = models.ForeignKey(User, related_name='acctype_modifiers', verbose_name=_('Modified by'),
                                       on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Account type')
        verbose_name_plural = _('Account types')

    def df_account_type(self):
        s_value = "{0}"
        return s_value.format(self.name)

    def __str__(self):
        return self.df_account_type()


class country(models.Model):
    code = models.CharField(max_length=6, default=0, verbose_name=_('Country code'))
    name = models.CharField(verbose_name=_('Country name'), max_length=255)

    createddate = models.DateTimeField(default=timezone.now, verbose_name=_('Created date'))
    createdby = models.ForeignKey(User, related_name='country_user', verbose_name=_('Created by'),
                                  on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True, verbose_name=_('Modified date'))
    lastmodifiedby = models.ForeignKey(User, related_name='country_modifiers', verbose_name=_('Modified by'),
                                       on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def df_countryname(self):
        s_value = "{0} - {1}"
        return s_value.format(self.code, self.name)

    def __str__(self):
        return self.df_countryname()


class city(models.Model):
    name = models.CharField(verbose_name=_('City name'), max_length=255)
    country = models.ForeignKey(country,
                                verbose_name=_('Country'),
                                related_name='city_country',
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    code = models.IntegerField(verbose_name=_('City Code'))

    createddate = models.DateTimeField(default=timezone.now, verbose_name=_('Created date'))
    createdby = models.ForeignKey(User,
                                  related_name='city_user',
                                  verbose_name=_('Created by'),
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True
                                  )
    lastmodifieddate = models.DateTimeField(auto_now_add=True, verbose_name=_('Modified date'))
    lastmodifiedby = models.ForeignKey(User,
                                       related_name='city_modifiers',
                                       verbose_name=_('Modified by'),
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       blank=True
                                       )

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

    createddate = models.DateTimeField(default=timezone.now, verbose_name=_('Created date'))
    createdby = models.ForeignKey(User,
                                  related_name='address_user',
                                  verbose_name=_('Created by'),
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True
                                  )
    lastmodifieddate = models.DateTimeField(auto_now_add=True, verbose_name=_('Modified date'))
    lastmodifiedby = models.ForeignKey(User,
                                       related_name='address_modifiers',
                                       verbose_name=_('Modified by'),
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       blank=True
                                       )

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        unique_together = ('name', 'city')

    def __str__(self):
        return self.name


class account(models.Model):
    name = models.CharField(max_length=65, verbose_name=_('Account name'))
    accountnumber = models.CharField(verbose_name=_('Account number'), max_length=18, unique=True, db_index=True)
    type = models.ForeignKey(account_type, on_delete=True, related_name='acc_acctype', verbose_name=_('Account Type'))
    company = models.ForeignKey(company, on_delete=models.CASCADE, verbose_name=_('Parent company'),
                                related_name='acc_company', parent_link=True, null=True)
    note = models.TextField(verbose_name=_('Notes'), null=True, blank=True)

    address = models.CharField(max_length=30, verbose_name=_('Address'), default='')
    addressnumber = models.CharField(max_length=6, verbose_name=_('Address number'), default=0)
    city = models.CharField(max_length=65, null=False, default='', verbose_name=_('City'))
    state = models.CharField(max_length=30, null=False, default='', verbose_name=_('State'))
    country = models.CharField(max_length=65, default='CHILE', null=True, verbose_name=_('Country'))

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='account_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='account_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def __str__(self):
        return self.name


class unit(models.Model):
    id = models.AutoField(primary_key=True)
    unitnumber = models.CharField(max_length=50, verbose_name=_('Unit number'))
    type = models.ForeignKey(account_type, on_delete=True, verbose_name=_('Account Type'))
    company = models.ForeignKey(company,
                                on_delete=models.CASCADE,
                                verbose_name=_('Parent company'),
                                related_name='unit_company',
                                parent_link=True,
                                null=True)

    aliquot = models.FloatField(verbose_name=_('Aliquot'))
    comments = models.TextField(null=True, blank=True)
    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='unit_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='unit_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

    class Meta:
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')
        unique_together = ('type', 'unitnumber')

    """def unitname(self):
        s_value = "{0} {1}"
        return s_value.format(self.type, self.unitnumber)"""

    def __str__(self):
        return self.unitnumber


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
    lastmodifiedby = models.ForeignKey(User, related_name='contact_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

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
