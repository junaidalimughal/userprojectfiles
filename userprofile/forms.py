from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class SignUp(UserChangeForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password", "is_active", "is_staff", "date_of_birth", "address"]

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ["first_name", "last_name", "email", "date_of_birth", "address"]


"""class CustomUserCreationForm(forms.Form):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={"placeholder":"Last Name"}))
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Enter Password", widget=forms.PasswordInput(attrs={"placeholder":"Enter Password"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={"type":"date", "placeholder":"Date of Birth"}))
    address = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    is_staff = forms.BooleanField()
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        if len(first_name) == 0:
            raise ValidationError("First Name can't be empty.")
        first_name = first_name.capitalize()
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        if len(last_name) == 0:
            raise ValidationError("Last Name can't be empty.")
        last_name = last_name.capitalize()
        return last_name
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        user_email = CustomUser.objects.filter(email=email)
        if user_email.count():
            raise ValidationError("A user name with this email already exists.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1'].lower()
        password2 = self.cleaned_data['password2'].lower()
         
        if (password1 and password2) and password1 != password2:
            raise ValidationError("Password don't match.")

        return password2
    
    def save(self, commit=True):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        password2 = self.cleaned_data['password2']
        date_of_birth = self.cleaned_data['date_of_birth']
        address = self.cleaned_data['address']
        is_staff = self.cleaned_data['is_staff']
        user = CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email, password=password2, date_of_birth=date_of_birth, address=address, is_staff=is_staff)
        return user

"""
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", 'first_name', 'last_name', 'address')