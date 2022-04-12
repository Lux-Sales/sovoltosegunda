from django.db import models


class Event(models.Model):
    # event data
    name = models.CharField(max_length=200, blank=False)
    ticket_value = models.DecimalField(
        decimal_places=2,
        blank=False,
        max_digits=10
    )
    description = models.TextField(blank=True)
    # location data
    cep = models.IntegerField(blank=False)
    public_place = models.CharField(max_length=200, blank=False)
    complement = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=200, blank=False)
