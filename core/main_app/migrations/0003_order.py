# Generated by Django 4.1.6 on 2023-02-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_menu_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Ваше имя')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('menu', models.ManyToManyField(to='main_app.menu')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
