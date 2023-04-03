from django.db import models

class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
