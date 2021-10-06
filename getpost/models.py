from django.db import models

# Create your models here.

class employees(models.Model):
    firtname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firtname
