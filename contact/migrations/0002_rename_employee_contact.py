# Generated by Django 5.1.1 on 2024-09-17 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Contact',
        ),
    ]
