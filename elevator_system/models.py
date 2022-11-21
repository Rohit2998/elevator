from django.db import models
import uuid

# Create your models here.
class Elevator(models.Model):
   elevatorID =models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
   currentfloor = models.IntegerField()
   requested_floor = models.IntegerField()
   elevator_status = models.CharField(max_length=100)
