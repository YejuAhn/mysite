from django.db import models
from django.utils import timezone
import datetime
from accounts.models import User
from polymorphic.models import PolymorphicModel

#############Question##############
class Question(models.Model):
    question_text = models.CharField(max_length=200, default = "PROVIDE QUESTION")
    question_desc = models.TextField()
    whyweask = models.TextField()

    def __str__(self):
        return self.question_text


##############Answer################
class Answer(PolymorphicModel):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Card(Answer):
    pass

class ShortAnswer(Answer):
    pass

class MC(Answer):
    pass


##############Options###############
class Option(models.Model):
    class Meta:
        abstract = True
    option_text = models.TextField(default = None)

    def __str__(self):
        return self.option_text

class Choice(Option):
    card = models.ForeignKey(Card, on_delete= models.CASCADE)
    mc = models.ForeignKey(MC, on_delete=models.CASCADE)

class StringInput(Option):
    stored_text = models.TextField()
    short_answer = models.ForeignKey(ShortAnswer, on_delete=models.CASCADE)

class Date(Option):
    date = models.DateField(auto_now_add=True)

class IntInput(Option):
    int_input = models.IntegerField(default=0)
    short_answer = models.ForeignKey(ShortAnswer, on_delete=models.CASCADE)

class FloatInput(Option):
    float_input = models.FloatField(default=0.0)
    short_answer = models.ForeignKey(ShortAnswer, on_delete=models.CASCADE)