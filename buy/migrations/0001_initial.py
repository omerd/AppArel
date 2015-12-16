# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.BigIntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCatalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='catalog_id',
            field=models.ForeignKey(to='buy.ProductCatalog'),
        ),
        migrations.AddField(
            model_name='buyhistory',
            name='product',
            field=models.ForeignKey(to='buy.Product'),
        ),
    ]
