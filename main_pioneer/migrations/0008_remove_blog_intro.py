# Generated by Django 3.0.8 on 2020-07-21 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_pioneer', '0007_auto_20200720_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='intro',
        ),
    ]
