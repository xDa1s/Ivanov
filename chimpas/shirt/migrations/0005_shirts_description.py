# Generated by Django 4.1.3 on 2022-12-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0004_alter_shirts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirts',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
