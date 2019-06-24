from django.test import Client
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User
import json


class BaseTestCase(object):
    _client = Client()

    def get_headers(self, headers, no_headers):
        if no_headers:
            return {}
        elif not headers:
            return {
                "HTTP_AUTHORIZATION": "Bearer {}".format(
                    AccessToken.for_user(User.objects.get(pk=1))
                )
            }
        return headers

    def graphql_query(
        self,
        query: str,
        variables: dict = None,
        headers: dict = None,
        no_headers: bool = False,
    ):
        return self._client.post(
            "/graphql",
            json.dumps({"query": query, "variables": variables}),
            content_type="application/json",
            **self.get_headers(headers, no_headers),
        )

    def get_request(self, url, headers: dict = None, no_headers: bool = False):
        return self._client.get(url, **self.get_headers(headers, no_headers))

    def post_request(
        self, url, data: dict = None, headers: dict = None, no_headers: bool = False
    ):
        return self._client.post(
            url,
            data,
            content_type="application/json",
            **self.get_headers(headers, no_headers),
        )
