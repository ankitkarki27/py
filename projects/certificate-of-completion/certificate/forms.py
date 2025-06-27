from django import forms
from django.utils import timezone

class CertificateForm(forms.Form):
    name = forms.CharField(label="Student Name", max_length=100)
    course_name = forms.CharField(label="Course Name", max_length=200)
    certificate_id = forms.CharField(label="Certificate ID", required=False)
    issued_at = forms.DateTimeField(
        label="Issued At",
        required=False,
        widget=forms.HiddenInput(),  # Hide the field in the form
        initial=timezone.now  # Set initial value to current time
    )
