# Generated by Django 4.0.1 on 2022-02-24 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='customer_name',
        ),
    ]
