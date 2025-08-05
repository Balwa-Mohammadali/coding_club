from .models import Apply,Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class applyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','branch','why']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','msg']