from graphene_django import DjangoObjectType
import graphene

from .models import Question
from .models import Choice 


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question 


'''
class QuestionType(graphene.ObjectType):
    question_text = graphene.String()
    pub_date = graphene.types.datetime.Datetime() 
'''


class ChoiceType(DjangoObjectType):
    class Meta: 
        model = Choice 


class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    question = graphene.Field(QuestionType, id=graphene.Int())

    def resolve_all_question(self, info):
        return Question.objects.all()

    def resolve_question(self, info, **kwargs):
        qid = kwargs.get('id')

        if qid is not None: 
            return Question.objects.get(pk=qid)
        return None 


schema = graphene.Schema(query=Query)