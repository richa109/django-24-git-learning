# Generated by Django 5.0.2 on 2024-03-12 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0005_goal_alter_account_created_at_expense_goalname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='goalname',
            new_name='goal_name',
        ),
    ]