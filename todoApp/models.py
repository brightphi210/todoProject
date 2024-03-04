from django.db import models

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
