# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0007_auto_20170413_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(help_text=b'Only inputy numbers, No Dash Marks', max_length=10),
        ),
    ]
