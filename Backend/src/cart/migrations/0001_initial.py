# Generated by Django 3.1 on 2020-08-12 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('product_quantity', models.IntegerField()),
            ],
        ),
    ]
