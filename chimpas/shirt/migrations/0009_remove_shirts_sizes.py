# Generated by Django 4.1.4 on 2022-12-10 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0008_remove_shirts_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shirts',
            name='sizes',
        ),
    ]
