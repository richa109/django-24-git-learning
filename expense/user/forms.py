from django import forms
from django.forms.widgets import Select
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import transaction
from.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'age', 'salary' , 'pic')
        

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_user = True
        if commit:
            user.save()
        return user
    