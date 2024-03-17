from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Expense)
admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(CurrencyType)
admin.site.register(Goal)