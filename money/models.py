from django.db import models

# Create your models here.
class user(models.Model):
    pid=models.IntegerField(10)
    nick=models.CharField(max_length=30)

    def __str__(self):
        return self.pid,self.nick