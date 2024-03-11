from django import forms
from.models import Expense
from .models import Account
# from user.models import User

class ExpCreationForm(forms.ModelForm):
    class Meta:
        model =Expense
        fields ='__all__'
        # exclude = ['user']
        
        widgets = {
            'expDateTime': forms.DateInput(attrs={'type': 'date'}),
        }
        
class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }