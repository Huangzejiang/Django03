from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=6)
    password = models.CharField(max_length=6)
    email = models.EmailField()


