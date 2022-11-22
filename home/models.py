from django.db import models

# Create your models here.

class Destination(models.Model):

    location = models.CharField(max_length=100)
    incident_desc = models.TextField()
    datetime = models.DateTimeField()
    incident_loc = models.TextField()
    initial_severity = models.CharField(max_length=100) 
    suspected_cause = models.TextField()
    immediate_actions_taken = models.TextField()
    #    sub_incident_types = models.CharField(max_length=100)
