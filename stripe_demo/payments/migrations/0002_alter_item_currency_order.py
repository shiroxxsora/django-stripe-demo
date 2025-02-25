# Generated by Django 5.1.6 on 2025-02-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR')], max_length=3),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR')], max_length=3)),
                ('items', models.ManyToManyField(to='payments.item')),
            ],
        ),
    ]
