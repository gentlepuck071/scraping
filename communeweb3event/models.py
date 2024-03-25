from django.db import models

class Web3event(models.Model):
    title = models.CharField(max_length = 100)
    image = models.CharField(max_length = 100)
    source_url = models.CharField(max_length = 100)
    event_url = models.CharField(max_length = 100)
    summary = models.CharField(max_length = 300)
    description = models.CharField()
    title = models.CharField(max_length = 100)
