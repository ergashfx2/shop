# Generated by Django 4.2.6 on 2023-11-26 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Qabul qilindi', 'Qabul qilindi'), ('Bekor qilindi', 'Bekor qilindi'), ('Yetkazilmoqda', 'Yetkazilmoqda'), ('Yetkazib berildi', 'Yetkazib berildi')], default='Qabul qilindi', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_location',
            field=models.CharField(choices=[('choice', 'Manzilni tanlash'), ('toshkent', 'Toshkent Shahri'), ('andijon', 'Andijon Viloyati'), ('buxoro', 'Buxoro Viloyati'), ('fargona', "Farg'ona Viloyati"), ('jizzax', 'Jizzax Viloyati'), ('qoraqalpogiston', "Qoraqalpog'iston Respublikasi"), ('namangan', 'Namangan Viloyati'), ('navoiy', 'Navoiy Viloyati'), ('samarqand', 'Samarqand Viloyati'), ('surxondaryo', 'Surxondaryo Viloyati'), ('toshkent_viloyati', 'Toshkent Viloyati'), ('xorazm', 'Xorazm Viloyati')], max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(max_length=150),
        ),
    ]
