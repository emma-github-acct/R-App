# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_auto_20170322_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='friday_close',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='friday_open',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='monday_close',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='monday_open',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='saturday_close',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='saturday_open',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='sunday_close',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='sunday_open',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='thursday_close',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='thursday_open',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='tuesday_close',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='tuesday_open',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='wednesday_close',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='wednesday_open',
            field=models.IntegerField(default=24, choices=[(24, 'CLOSED'), (0, '12 am'), (1, '1 am'), (2, '2 am'), (3, '3 am'), (4, '4 am'), (5, '5 am'), (6, '6 am'), (7, '7 am'), (8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'), (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'), (19, '7 pm'), (20, '8 pm'), (21, '9 pm'), (22, '10 pm'), (23, '11 pm')]),
        ),
    ]
