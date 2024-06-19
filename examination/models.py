from datetime import datetime

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Person(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birth_day = models.DateField(default=datetime(year=2000, month=1, day=1))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
