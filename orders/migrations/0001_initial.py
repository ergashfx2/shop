# Generated by Django 4.2.6 on 2023-11-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=200)),
                ('customer_location', models.CharField(max_length=200)),
            ],
        ),
    ]
