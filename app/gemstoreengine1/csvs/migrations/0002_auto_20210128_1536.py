# Generated by Django 3.1.5 on 2021-01-28 15:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv',
            name='activated',
        ),
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.FileField(blank=True, help_text='Допускаются только файлы формата .csv', null=True, upload_to='csvs', validators=[django.core.validators.FileExtensionValidator(['csv'])]),
        ),
    ]
