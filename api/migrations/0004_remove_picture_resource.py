# Generated by Django 5.0.6 on 2024-05-14 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_picture_resource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='resource',
        ),
    ]
