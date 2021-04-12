# Generated by Django 3.2 on 2021-04-11 02:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('submitter', '0003_auto_20210411_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='test_enable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='limit',
            field=models.DateField(default=datetime.datetime(2021, 4, 11, 2, 15, 25, 459503, tzinfo=utc), verbose_name='Submit limit'),
        ),
    ]