# Generated by Django 5.0.2 on 2024-03-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='catname',
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='expense',
            name='subCategory',
            field=models.CharField(),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
