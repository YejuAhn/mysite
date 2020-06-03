from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Choice, Question, StringInput, IntInput, Date, FloatInput, Card, ShortAnswer, MC
from django.utils.safestring import mark_safe
from django.urls import reverse

##OPTIONS
class CardChoiceInline(NestedStackedInline):
    model = Choice
    extra = 1
    fk_name = 'card'

class StringInputInline(NestedStackedInline):
    model = StringInput
    extra = 1
    fk_name = 'short_answer'

class IntInputLine(NestedStackedInline):
    model = IntInput
    extra = 1
    fk_name = 'short_answer'

class ShortAnswerInline(NestedStackedInline):
    model = ShortAnswer
    extra = 1
    fk_name = 'short_answer_question'
    inlines = [StringInputInline, IntInputLine]


##ANSWER
class CardInline(NestedStackedInline):
    model = Card
    extra = 1
    fk_name = 'card_question'
    inlines = [CardChoiceInline]

##QUESTION
class QuestionAdmin(NestedModelAdmin):
    model = Question
    inlines = [CardInline, ShortAnswerInline]

admin.site.register(Question, QuestionAdmin)




