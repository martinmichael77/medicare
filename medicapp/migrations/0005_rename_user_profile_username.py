# Generated by Django 4.2.4 on 2023-08-17 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicapp', '0004_delete_tbl_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]
