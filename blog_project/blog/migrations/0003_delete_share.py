# Generated by Django 2.2 on 2020-05-31 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200530_1954'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Share',
        ),
    ]