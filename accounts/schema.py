from .models import User
from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
import graphql_jwt

class UserType(DjangoObjectType):
    class Meta:
        model = User

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required = True)
        username = graphene.String(required = True)

    def mutate(self, info, email, username):
        user = get_user_model()(
            email = email,
            username = username
        )
        user.save()
        return CreateUser(user = user)


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
    user = graphene.Field(UserType, email = graphene.String())

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, email):
        return User.objects.get(email = email)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return user



class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


#customizing tokenauth
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


