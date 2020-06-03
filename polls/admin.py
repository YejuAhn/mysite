from django.contrib import admin
import nested_admin
from .models import Choice, Question, Card, ShortAnswer, StringInput, IntInput, FloatInput, MC, Answer
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline


class ChoiceInline(nested_admin.NestedStackedInline):
    model = Choice

class StringInputInline(nested_admin.NestedStackedInline):
    model = StringInput

class IntInputInline(nested_admin.NestedStackedInline):
    model = IntInput

class FloatInputInline(nested_admin.NestedStackedInline):
    model = FloatInput

class AnswerInline(nested_admin.NestedStackedPolymorphicInline):
    class CardInline(nested_admin.NestedStackedPolymorphicInline.Child):
        model = Card
        inlines = [ChoiceInline]

    class ShortAnswerInline(nested_admin.NestedStackedPolymorphicInline.Child):
        model = ShortAnswer
        inlines = [StringInputInline, IntInputInline, FloatInputInline]

    class MCInline(nested_admin.NestedStackedPolymorphicInline.Child):
        model = MC
        inlines = [ChoiceInline]

    model = Answer
    child_inlines = (
            CardInline,
            ShortAnswerInline,
            MCInline
    )

@admin.register(Question)
class QuestionAdmin(nested_admin.NestedPolymorphicModelAdmin):
    inlines = [AnswerInline]

