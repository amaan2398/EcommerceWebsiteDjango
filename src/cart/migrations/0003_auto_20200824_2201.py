# Generated by Django 3.1 on 2020-08-24 22:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200824_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='date_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
