# Generated by Django 3.2.7 on 2022-09-22 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]