from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Photo(models.Model):
    image = models.ImageField()
    upvotes = models.ManyToManyField(User, related_name = 'upvotes')
    downvotes = models.ManyToManyField(User, related_name = 'downvotes')

    def upvote(self, user):
	self.upvotes.add(user)

    def remove_upvote(self, user):
        self.upvotes.remove(user)

    def downvote(self, user):
        self.downvotes.add(user)

    def remove_downvote(self, user):
        self.downvotes.remove(user)

    def is_upvoted(self, user):
	try:
           user = self.upvotes.get(id=user.id)
	   if user:
		return True
	   else:
		return False
        except ObjectDoesNotExist:
           return False

    def is_downvoted(self, user):
        try:
           user = self.downvotes.get(id=user.id)
           if user:
                return True
           else:
                return False
        except ObjectDoesNotExist:
           return False
