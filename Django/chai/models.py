from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA CHAI'),
        ('GR', 'GINGER'),
        ('KK', 'KASHRMI KAHWA'),
        ('BL', 'BLACK'),
        ('GC', 'GREEN CHAI'),
        ('NC', 'NOON CHAI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)