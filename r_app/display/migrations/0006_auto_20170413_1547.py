# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0005_auto_20170411_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='fax_number',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default=9999999999, max_length=11),
        ),
    ]
