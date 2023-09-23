from django import forms
from app1.models import Enquiry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('name','phone','email','courses')

class EditForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')