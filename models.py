from django.db import models

# Create your models here.

class Members(models.Model):
   
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length= 200)
    start_time = models.DateTimeField(auto_now_add= True)
    end_time = models.DateTimeField(auto_now_add= True)