from django.db import models
from datetime import datetime

# Create your models here
class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    #position = models.ForeignKey('Position', on_delete = models.CASCADE, null = True, blank = True)
    birthdate = models.DateField()
    platform = models.TextField()


class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Vote(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete = models.CASCADE, null = True, blank = True, related_name = 'vote')
    vote_datetime = models.DateTimeField(default=datetime.now())
    votes = models.IntegerField(default=0)
