import graphene
from api.graphql.queries import GetUser


class Query(GetUser, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
