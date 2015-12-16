# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_auto_20151103_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcatalog',
            name='price',
            field=models.PositiveIntegerField(default=500),
        ),
    ]
