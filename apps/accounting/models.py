from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.appweb.models import company
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class bank_account(models.Model):
    reference = models.CharField(verbose_name=_('Reference Bank Account'), max_length=12, null=False,
                                 primary_key=True, unique=True)
    label = models.CharField(max_length=30, verbose_name=_('Label Bank Account'), null=False, unique=True)

    entity = models.IntegerField(null=False, default=1 )
    companyid = models.ForeignKey(company, verbose_name=_('Company'), null=True, on_delete=models.SET_NULL)
    bankname = models.CharField(max_length=60, verbose_name=_('Bank Name'))
    bankcode = models.CharField(max_length=125, verbose_name=_('Bank Code'), unique=True )
    number = models.CharField(max_length=255, verbose_name=_('Number Bank Account') )

    accountcurrency = models.CharField(max_length=10 )
    mim_allowed = models.FloatField(default=0, max_length=11)
    mim_desired = models.FloatField(default=0, max_length=11)

    comments = models.TextField()

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='bankacc_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='bankacc_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

    class Meta:
        verbose_name = _('Bank Account')
        verbose_name_plural = _('Bank Accounts')
        unique_together = ('reference', 'label')

    def bankname(self):
        s_value = "{0} ({1})"
        return s_value.format(self.label, self.accountcurrency)

    def __str__(self):
        return self.bankname()

class trans(models.Model):
    transcode = models.CharField(verbose_name=_('Trans Code Ref'), max_length=18, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    dateoperation = models.DateTimeField(default=timezone.now)
    datevalue = models.DateTimeField(default=timezone.now)

    amount = models.FloatField(default=0.000000)
    description = models.CharField(max_length=60)
    bankaccount = models.ForeignKey(bank_account, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, verbose_name=_('Owner'), related_name='transowner_user', on_delete=models.SET_NULL, null=True )

    note = models.TextField(null=True)

    createddate = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, related_name='trans_user', on_delete=models.SET_NULL, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)
    lastmodifiedby = models.ForeignKey(User, related_name='trans_modifiers', on_delete=models.SET_NULL, null=True,
                                       blank=True)

    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
        unique_together = ('transcode', 'date')

    def trans_list(self):
        s_value = "{0} {1} {2}"
        return s_value.format(self.transcode, self.date, self.amount)

    def __str__(self):
        return self.trans_list()

