from django import forms

class CertificateForm(forms.Form):
    name = forms.CharField(max_length=100, label='write your name')
