from django import forms
from django.core import validators

def check_for_z(value):
    print("VALUE:",value)
    if value[0].lower()!='z':
        raise forms.ValidationError("name shouLd start with z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    verify_email=forms.EmailField(label="Enter your email again")

    def clean(self):
        cleaned_data = super().clean()  
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("verify_email")

        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError(
                "Emails do not match!",
                code="email_mismatch"
            )
        return cleaned_data 