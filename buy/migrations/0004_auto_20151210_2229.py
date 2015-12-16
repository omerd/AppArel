# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_productcatalog_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyhistory',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 12, 10, 20, 29, 48, 490000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyhistory',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
