# Generated by Django 2.0.3 on 2018-03-16 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxsign', '0005_otp_check_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Otp_check',
            new_name='Otp_match',
        ),
    ]
