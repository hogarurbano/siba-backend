"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from apps.appweb import models

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': _('Email  ')}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': _('Contraseña')}))


class AccountEntryForm(forms.ModelForm):
    class Meta:
        model = models.account
        fields = ['name', 'city', 'country', 'createdby']
        exclude = ['lastmodifieddate', 'modifiedby']

    def clean_author(self):
        if not self.cleaned_data['createdby']:
            return User()
        return self.cleaned_data['createdby']

    def clean_last_modified_by(self):
        if not self.cleaned_data['lastmodifiedby']:
            return User()
        return self.cleaned_data['lastmodifiedby']

class CityForm(forms.ModelForm):
    class Meta:
        model = models.city
        fields = ['name', 'country', 'createdby']
        exclude = ['lastmodifieddate', 'modifiedby']

    def clean_author(self):
        if not self.cleaned_data['createdby']:
            return User()
        return self.cleaned_data['createdby']

    def clean_last_modified_by(self):
        if not self.cleaned_data['lastmodifiedby']:
            return User()
        return self.cleaned_data['lastmodifiedby']