# Generated by Django 3.1.5 on 2021-01-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0002_auto_20210128_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]