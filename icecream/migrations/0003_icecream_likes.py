# Generated by Django 2.2.6 on 2019-10-09 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0002_auto_20191008_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
