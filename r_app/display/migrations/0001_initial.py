# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desk_name', models.CharField(max_length=40)),
                ('contact_name', models.CharField(max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('fax_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventsCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_title', models.CharField(max_length=50)),
                ('event_information', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('opening_time', models.IntegerField(default=9)),
                ('closing_time', models.IntegerField(default=5)),
                ('room_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ExceptionsCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('opening_time', models.IntegerField(default=9)),
                ('closing_time', models.IntegerField(default=5)),
                ('event_title', models.ForeignKey(to='display.EventsCalendar', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_title', models.CharField(max_length=20)),
                ('map_id', models.IntegerField(default=0, unique=True)),
                ('monday_open', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('monday_close', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('tuesday_open', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('tuesday_close', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('wednesday_open', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('wednesday_close', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('thursday_open', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('thursday_close', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('friday_open', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('friday_close', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('saturday_open', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('saturday_close', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('sunday_open', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
                ('sunday_close', models.IntegerField(default=24, choices=[(24, b'CLOSED'), (0, b'12 am'), (1, b'1 am'), (2, b'2 am'), (3, b'3 am'), (4, b'4 am'), (5, b'5 am'), (6, b'6 am'), (7, b'7 am'), (8, b'8 am'), (9, b'9 am'), (10, b'10 am'), (11, b'11 am'), (12, b'12 pm'), (13, b'1 pm'), (14, b'2 pm'), (15, b'3 pm'), (16, b'4 pm'), (17, b'5 pm'), (18, b'6 pm'), (19, b'7 pm'), (20, b'8 pm'), (21, b'9 pm'), (22, b'10 pm'), (23, b'11 pm')])),
            ],
        ),
        migrations.AddField(
            model_name='exceptionscalendar',
            name='location_title',
            field=models.ForeignKey(to='display.Location'),
        ),
        migrations.AddField(
            model_name='eventscalendar',
            name='location_title',
            field=models.ForeignKey(to='display.Location'),
        ),
        migrations.AddField(
            model_name='contact',
            name='location_title',
            field=models.ForeignKey(to='display.Location'),
        ),
    ]
