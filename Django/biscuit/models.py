from django.db import models
from django.utils import timezone

# Create your models here.
class BiscuitVarity(models.Model):
    BISCUIT_TYPE_CHOICE = [
        ('MG', 'Marie Gold'),
        ('GD', 'Good Day'),
        ('HS', 'Hide & Seek'),
        ('BB', 'Bourbon'),
        ('KJ', 'Krackjack'),
        ('OO', 'Oreo'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='biscuit/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=BISCUIT_TYPE_CHOICE)