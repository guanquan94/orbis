from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    Full_Name = models.CharField(max_length=1230, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #Python 3.3 is __str__
        return self.email