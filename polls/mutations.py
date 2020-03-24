from django.utils.timezone import now 

import graphene

from .models import Question
from .types import QuestionType 


class CreateQuestion(graphene.Mutation):
    class Arguments:
        question_text = graphene.String() 

    ok = graphene.Boolean()
    question = graphene.Field(QuestionType)

    def mutate(self, info, question_text):
        question = Question(question_text=question_text,
        pub_date=now()).save()
        ok = True
        return CreateQuestion(question=question,
        ok=ok)


class MyMutations(graphene.ObjectType):
    create_question = CreateQuestion.Field() 
    