from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from apps.accounting import models

class TransForm(forms.ModelForm):
    class Meta:
        model = models.trans
        fields = ['transcode', 'dateoperation', 'datevalue', 'amount', 'bankaccount', 'owner']
        exclude = ['lastmodifieddate', 'modifiedby']

    def clean_author(self):
        if not self.cleaned_data['createdby']:
            return User()
        return self.cleaned_data['createdby']

    def clean_last_modified_by(self):
        if not self.cleaned_data['lastmodifiedby']:
            return User()
        return self.cleaned_data['lastmodifiedby']