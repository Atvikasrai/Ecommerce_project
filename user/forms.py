from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer

# ----------------------------------------------------------------------------------------------------

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget =forms.TextInput(attrs={'autofocus' : 'True' , 'class' : 'form-control'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# ----------------------------------------------------------------------------------------------------

class LoginForm(AuthenticationForm):
    username = UsernameField(widget =forms.TextInput(attrs={'autofocus' : 'True' , 'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'}))


#------------------------------------------------------------------------------------------------------

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = 'Old Password', widget = forms.PasswordInput(attrs={'autofocus' : 'True', 'autocomplete' : 'current - password', 'class':'form-control'}))
    
    new_password1 = forms.CharField(label = 'New Password', widget = forms.PasswordInput(attrs={'autocomplete' : 'current - password', 'class':'form-control'}))
    
    new_password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput(attrs={'autocomplete' : 'current - password', 'class':'form-control'}))



#------------------------------------------------------------------------------------------------------

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


class PasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


#------------------------------------------------------------------------------------------------------

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'contact', 'email', 'locality', 'city', 'pincode','state',]
        widgets ={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}), 
            'contact':forms.TextInput(attrs={'class':'form-control'}), 
            'email':forms.TextInput(attrs={'class':'form-control'}), 
            'locality':forms.TextInput(attrs={'class':'form-control'}), 
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            
        }