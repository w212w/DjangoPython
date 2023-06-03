from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True  # Оставляем поле логина обязательным
        self.fields['password'].required = True  # Оставляем поле пароля обязательным
        self.fields['username'].widget.attrs['autofocus'] = True  # Устанавливаем фокус на поле логина

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data