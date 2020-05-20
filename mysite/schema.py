import graphene

import polls.schema

#this class will inherit from multiple Queries
#as we begin to add more apps to our project
class Query(polls.schema.Query, graphene.ObjectType):
    pass


class Mutation(polls.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation = Mutation)
