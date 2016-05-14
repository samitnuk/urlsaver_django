from django.db import models

from django.contrib.auth.models import User

# class with name URL does not work with Flask in previous project
# (URL - Uniform Resource Locator)
class Locator(models.Model):
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    groupname = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
