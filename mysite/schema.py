import graphene
import polls.schema
import accounts.schema
import graphql_jwt
from accounts.schema import ObtainJSONWebToken

#this class will inherit from multiple Queries
#as we begin to add more apps to our project
class Query(polls.schema.Query, accounts.schema.Query ,graphene.ObjectType):
    pass



#creates token authorization for us
class Mutation(polls.schema.Mutation, accounts.schema.Mutation, graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation = Mutation)
