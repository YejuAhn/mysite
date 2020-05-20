from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from polls.models import Question

from .serializers import QuestionSerializer


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class QuestionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
