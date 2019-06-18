from graphene_django.types import DjangoObjectType
from django.apps import apps


class UserType(DjangoObjectType):
    class Meta:
        model = apps.get_model("users", "user")
        # exclude_fields = ('password', )
