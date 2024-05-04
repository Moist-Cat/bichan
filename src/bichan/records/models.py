from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Record(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    
    def __str__(self):
        return f"<({self.__class__.__name__}) {self.name=} {self.value=}>"

