from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email']

        widgets = {
    'name': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter name'
    }),
    'phone': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter phone'
    }),
    'email': forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email'
    }),
}

