# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catalog_id',
            new_name='catalog',
        ),
    ]
