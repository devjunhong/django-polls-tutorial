import graphene

from .models import Question
from .models import Choice 
from .types import QuestionType
from .types import ChoiceType
from .types import CustomType


class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    question = graphene.Field(QuestionType, id=graphene.Int())
    custom_question = graphene.Field(CustomType, 
    id=graphene.Int())

    def resolve_all_questions(self, info):
        return Question.objects.all()

    def resolve_question(self, info, **kwargs):
        qid = kwargs.get('id')

        if qid is not None: 
            return Question.objects.get(pk=qid)
        return None 

    def resolve_custom_question(self, info, **kwargs):
        qid = kwargs.get('id')

        cq = CustomType()
        if qid is not None:
            question = Question.objects.get(pk=qid)
            cq.question = question
            cq.message = "Query Succeeded!"
            return cq 
        return None


schema = graphene.Schema(query=Query)