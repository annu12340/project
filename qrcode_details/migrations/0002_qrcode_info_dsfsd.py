# Generated by Django 3.2.8 on 2023-01-08 05:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode_info',
            name='dsfsd',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
