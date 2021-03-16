# Generated by Django 3.1.6 on 2021-03-15 15:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210312_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='rent',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000)]),
        ),
    ]