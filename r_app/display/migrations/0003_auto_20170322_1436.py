# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_auto_20170322_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='fax_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
