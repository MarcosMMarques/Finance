# Generated by Django 4.2.3 on 2023-07-03 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoy',
            new_name='Category',
        ),
    ]