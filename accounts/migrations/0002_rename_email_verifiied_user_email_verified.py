# Generated by Django 5.0.3 on 2025-02-23 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_verifiied',
            new_name='email_verified',
        ),
    ]
