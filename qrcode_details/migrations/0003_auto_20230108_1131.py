# Generated by Django 3.2.8 on 2023-01-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode_details', '0002_qrcode_info_dsfsd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='qrcode_info',
            name='dsfsd',
        ),
        migrations.RemoveField(
            model_name='qrcode_info',
            name='user_id',
        ),
    ]
