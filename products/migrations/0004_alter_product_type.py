# Generated by Django 4.2.6 on 2023-11-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Ayollar', 'Ayollar'), ('Erkaklar', 'Erkaklar'), ('Bolalar', 'Bolalar'), ("Uy-Xo'jalik", "Uy-Xo'jalik"), ('Salomatlik', 'Salomatlik')], default='none', max_length=20),
        ),
    ]
