# Generated by Django 5.1.6 on 2025-02-25 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_discount_tax_order_discount_order_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='name',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='percentage_off',
        ),
    ]
