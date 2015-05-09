from django.db import models

# Create your models here.
class Question(models.Model):
    image = models.ImageField()
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
