from django.db import models


class Note(models.Model):
    content = models.TextField(blank=True, max_length=20000)
