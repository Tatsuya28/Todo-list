from django.db import models

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField()


class Task(models.Model):
    description = models.CharField(max_length=512)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
