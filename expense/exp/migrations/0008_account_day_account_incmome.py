# Generated by Django 5.0.2 on 2024-03-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0007_rename_goal_name_expense_goal_alter_goal_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='day',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='incmome',
            field=models.FloatField(null=True),
        ),
    ]
