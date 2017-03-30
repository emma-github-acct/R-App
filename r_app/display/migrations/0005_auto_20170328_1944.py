# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_auto_20170323_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normalhours',
            name='location_title',
        ),
        migrations.DeleteModel(
            name='NormalHours',
        ),
    ]
