from django.db import models
from django.contrib.auth.models import Group

class Record(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    role = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="records")
    
    def __str__(self):
        return f"<({self.__class__.__name__}) {self.name=} ; {self.value=} ; {self.role.name=}>"
