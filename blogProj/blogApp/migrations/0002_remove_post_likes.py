# Generated by Django 4.0.2 on 2022-02-15 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]