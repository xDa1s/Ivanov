# Generated by Django 4.1.4 on 2022-12-10 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0007_alter_shirts_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shirts',
            name='size',
        ),
    ]