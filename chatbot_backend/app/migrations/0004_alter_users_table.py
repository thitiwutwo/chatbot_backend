# Generated by Django 4.1.7 on 2023-03-02 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_user_users'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='users',
            table='Users',
        ),
    ]
