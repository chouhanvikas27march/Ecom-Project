from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, UsernameField , PasswordChangeForm , SetPasswordForm , PasswordResetForm , SetPasswordForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


# signup
class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(label="email",widget = forms.EmailInput(attrs={'class':'form-control'}), required=True)
    password1 = forms.CharField(label="password",widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password (again)",widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
        fields = ("username","email","password1","password2")
        
#login
class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True , 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),)

#changepassword_with_old_pass

class UserChangePass(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True , 'class':'form-control'}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )    

    field_order = ['old_password', 'new_password1', 'new_password2']

#UserPasswordResetForm

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'})
    )
#setpasswordon mail

class UserSetPasswordForm(SetPasswordForm):
     new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
     new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )


