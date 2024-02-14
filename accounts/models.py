from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import strong_password

from django.contrib.auth.forms import UserCreationForm


class RegisterUser(UserCreationForm):

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Username', 'class': 'input-label-input'}
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'input-label-input'}
        ),
        error_messages={'unique': 'This email is already in use'}
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password', 'class': 'input-label-input'}
        ),
        error_messages={'required': 'This field not must by empty'},
        validators=[strong_password]
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class': 'input-label-input'
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'username',
        ]

    def clean_email(self):
        data = self.cleaned_data.get('email')
        user = User.objects.filter(email=data).exists()

        if user:
            raise ValidationError(
                'This email is already in use',
                code='unique'
            )
        return data

    def clean(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password2 is not None:
            if password1 != password2:
                self.add_error('password2', 'passwords must be the same')
            return self.cleaned_data
        return cleaned_data


class LoginUser(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Username', 'class': 'input-label-input'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'password', 'class': 'input-label-input'}
        )
    )
