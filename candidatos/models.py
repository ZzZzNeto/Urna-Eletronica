from django.db import models

class Candidate(models.Model):
    
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=5, unique=True)
    votes = models.IntegerField(default=0)


