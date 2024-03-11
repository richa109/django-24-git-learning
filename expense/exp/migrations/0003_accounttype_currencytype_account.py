# Generated by Django 5.0.2 on 2024-03-08 05:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0002_remove_subcategory_catname_alter_expense_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'accounttype',
            },
        ),
        migrations.CreateModel(
            name='CurrencyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'currencytype',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('balance', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('accounttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp.accounttype')),
                ('currencytype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp.currencytype')),
            ],
            options={
                'db_table': 'account',
            },
        ),
    ]