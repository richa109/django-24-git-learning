# Generated by Django 5.0.2 on 2024-03-12 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0004_alter_account_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goalname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Goal',
            },
        ),
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='goalname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exp.goal'),
        ),
    ]
