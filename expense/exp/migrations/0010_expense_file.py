# Generated by Django 5.0.2 on 2024-04-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0009_rename_incmome_account_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]