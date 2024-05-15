# Generated by Django 5.0.6 on 2024-05-14 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='additional_data',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='copyright',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='picture',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]