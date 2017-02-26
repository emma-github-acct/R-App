from django.db import models

class Location(models.Model):
    location_title = models.CharField(max_length=20, default="Default")
    map_number = models.IntegerField(default=0)
    contact = models.IntegerField(default=0)
    
class Calendar(models.Model):
    MIDNIGHT = 24
    ONE_AM = 1
    TWO_AM = 2
    THREE_AM = 3
    FOUR_AM = 4
    FIVE_AM =5
    SIX_AM = 6
    SEVEN_AM = 7
    EIGHT_AM = 8
    NINE_AM = 9
    TEN_AM = 10
    ELEVEN_AM = 11
    NOON = 12
    ONE_PM = 13
    TWO_PM = 14
    THREE_PM = 15
    FOUR_PM = 16
    FIVE_PM = 17
    SIX_PM = 18
    SEVEN_PM = 19
    EIGHT_PM = 20
    NINE_PM = 21
    TEN_PM = 22
    ELEVEN_PM = 23
    HOUR_CHOICES = (
        (MIDNIGHT, '12 am'),
        (ONE_AM, '1 am'),
        (TWO_AM, '2 am'),
        (THREE_AM, '3 am'),
        (FOUR_AM, '4 am'),
        (FIVE_AM, '5 am'),
        (SIX_AM, '6 am'),
        (SEVEN_AM, '7 am'),
        (EIGHT_AM, '8 am'),
        (NINE_AM, '9 am'),
        (TEN_AM, '10 am'),
        (ELEVEN_AM, '11 am'),
        (NOON, '12 pm'),
        (ONE_PM, '1 pm'),
        (TWO_PM, '2 pm'),
        (THREE_PM, '3 pm'),
        (FOUR_PM, '4 pm'),
        (FIVE_PM, '5 pm'),
        (SIX_PM, '6 pm'),
        (SEVEN_PM, '7 pm'),
        (EIGHT_PM, '8 pm'),
        (NINE_PM, '9 pm'),
        (TEN_PM, '10 pm'),
        (ELEVEN_PM, '11 pm'),
    )
    location = models.ForeignKey(
        "Location",
        on_delete=models.CASCADE,
    )
    monday_open = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    monday_close = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    tuesday_open = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    tuesday_close = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    wednesday_open = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    wednesday_close = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    thursday_open = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    thursday_close = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    friday_open = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    friday_close = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    saturday_open = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    saturday_close = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    sunday_open = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    sunday_close = models.IntegerField(
        choices=HOUR_CHOICES,
        default=24,
    )
    
    