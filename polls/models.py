from django.db import models
from django.utils import timezone
import datetime
from accounts.models import User

class Question(models.Model):

    question_text = models.CharField(max_length=200, default = "PROVIDE QUESTION")
    # human-readable name
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    # tells Django each Choice is related to a single Question.
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, null = True, blank = True)
    choice_text = models.CharField(max_length=200, default = "PROVIDE CHOICE")
    #vote tally
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text




