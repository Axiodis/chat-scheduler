# Generated by Django 3.2.8 on 2021-10-14 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20211014_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='timezone',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='store',
            name='timezone',
            field=models.CharField(max_length=30),
        ),
    ]