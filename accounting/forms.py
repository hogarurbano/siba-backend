from django import forms
from . import models
from django.contrib.auth.models import User


class BankAcctForm(forms.ModelForm):
    class Meta:
        model = models.bank_account
        fields = ['accountreference', 'accountlabel', 'companyid', 'bankname', 'bankcode', 'accountnumber',
                  'accountcurrency', 'mim_allowed', 'mim_desired', 'comments', 'createddate', 'createdby']
        exclude = ['lastmodifieddate', 'modifiedby']

    def clean_owner(self):
        if not self.cleaned_data['createdby']:
            return User()
        return self.cleaned_data['createdby']

    def clean_last_modified_by(self):
        if not self.cleaned_data['lastmodifiedby']:
            return User()
        return self.cleaned_data['lastmodifiedby']

class TransForm(forms.ModelForm):
    class Meta:
        model = models.trans
        fields = ['transcode', 'dateoperation', 'datevalue', 'amount', 'bankaccount', 'owner']
        exclude = ['lastmodifieddate', 'modifiedby']

    def clean_owner(self):
        if not self.cleaned_data['createdby']:
            return User()
        return self.cleaned_data['createdby']

    def clean_last_modified_by(self):
        if not self.cleaned_data['lastmodifiedby']:
            return User()
        return self.cleaned_data['lastmodifiedby']