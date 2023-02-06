from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

