import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoFormMutation

from graphene_django.types import DjangoObjectType
from .models import Question, Choice

# class QuestionType(DjangoObjectType):
#     class Meta:
#         model = Question
#         filter_fields = ['name', 'pub_date']
#         interfaces = (graphene.relay.Node,)

class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        filter_fields = {
            'question_text' : ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )

class ChoiceNode(DjangoObjectType):
    class Meta:
        model = Choice
        filter_fields = {
            'choice_text': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )


class QuestionInput(graphene.InputObjectType):
    id = graphene.ID()
    question_text = graphene.String()
    pub_date = graphene.DateTime()

class CreateQuestion(graphene.Mutation):
    class Arguments:
        question_text = graphene.String()
        pub_date = graphene.DateTime()
    question = graphene.Field(QuestionNode)

    @staticmethod
    def mutate(root, info, question_text, pub_date):
        question_instance = Question(question_text = question_text, pub_date = pub_date)
        question_instance.save()
        return CreateQuestion(question = question_instance)


class Query(graphene.ObjectType):
    # questions = graphene.List(QuestionType)
    # question = graphene.Field(QuestionType, question_id = graphene.String())
    question = graphene.relay.Node.Field(QuestionNode)
    choice = graphene.relay.Node.Field(ChoiceNode)
    all_questions = DjangoFilterConnectionField(QuestionNode)
    all_choices = DjangoFilterConnectionField(ChoiceNode)

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_question(self, info, question_id):
        return Question.objects.get(pk = question_id)

    def resolve_choices(self, info, **kwargs):
        return Choice.objects.all()

    def resolve_choice(self, info, choice_id):
        return Choice.objects.get(pk = choice_id)


class Mutation(graphene.ObjectType):
    create_question = CreateQuestion.Field()




