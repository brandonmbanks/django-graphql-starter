import graphene
from api.graphql.types.user.user_type import UserType
from users.models import User


class GetUser(object):
    user = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user(self, info, **kwargs):
        id = kwargs["id"]
        user = User.objects.filter(pk=id).first()
        if not user:
            raise Exception(f"User {id} does not exist")
        return user
