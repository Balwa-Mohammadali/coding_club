from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    branch = models.CharField(max_length=25)
    why = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Contact(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    msg = models.TextField(max_length=300)

    def __str__(self):
        return self.name