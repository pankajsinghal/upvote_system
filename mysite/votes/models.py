from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    image = models.ImageField()
    upvotes = models.ManyToManyField(User, related_name = 'upvotes')
    downvotes = models.ManyToManyField(User, related_name = 'downvotes')
