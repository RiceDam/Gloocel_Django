from django.db import models

# Create your models here.
class Suite(models.Model):
    id = models.IntegerField(primary_key=True)
    suite_number = models.CharField(max_length=255)
    version = models.IntegerField()




