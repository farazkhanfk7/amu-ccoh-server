from django.db import models
from datetime import datetime
from django.utils import timezone
from multiselectfield import MultiSelectField

# Create your models here.
BOOL_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No')
]

TYPE_CHOICES = [
    ('Seller', 'Seller'),
    ('Filling', 'Filling Only'),
    ('Both', 'Both Available')
]

TAGS = [
    ('ICU', 'ICU'),
    ('BEDS','BEDS'),
    ('VENTILATOR','VENTILATOR')
]

class Hospital(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=200, blank=True, default='')
    contact = models.CharField(max_length=30, blank=True, default='')
    other_contact = models.CharField(max_length=30, blank=True, default='')
    availablity = models.CharField(choices=BOOL_CHOICES, max_length=10)
    tags = MultiSelectField(choices=TAGS)
    remarks = models.TextField(blank=True)
    created_on = models.DateTimeField(default=datetime.now())
    last_updated = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.name}"
    
    def save(self):
        self.last_updated = datetime.now()
        super(Hospital, self).save()


class OxygenSupplier(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=200, blank=True, default='')
    contact = models.CharField(max_length=30, blank=True, default='')
    other_contact = models.CharField(max_length=30, blank=True, default='')
    type_is = models.CharField(choices=TYPE_CHOICES, max_length=10)
    availablity = models.CharField(choices=BOOL_CHOICES, max_length=10)
    remarks = models.TextField(blank=True)
    created_on = models.DateTimeField(default=datetime.now())
    last_updated = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.name}"

    def save(self):
        self.last_updated = datetime.now()
        super(OxygenSupplier, self).save()
    