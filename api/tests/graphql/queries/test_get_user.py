import pytest
from utils import BaseTestCase


@pytest.mark.django_db()
class TestGetUser(BaseTestCase):
    def test_it_should_return_user(self, django_db_setup):
        res = self.graphql_query(
            """
            {
                user (id: 1) {
                    id
                    username
                    email
                }
            }
        """
        )
        user = res.json()["data"]["user"]
        assert "1" == user["id"]
        assert "admin" == user["username"]
        assert "admin@example.com" == user["email"]

    def test_it_should_error_if_user_does_not_exist(self):
        res = self.graphql_query(
            """
            {
                user (id: 2) {
                    id
                    username
                    email
                }
            }
        """
        )
        assert "User 2 does not exist" == res.json()["errors"][0]["message"]
        assert res.json()["data"]["user"] is None

    def test_it_should_not_allow_querying_for_password(self, django_db_setup):
        res = self.graphql_query(
            """
            {
                user (id: 1) {
                    id
                    username
                    email
                    password
                }
            }
        """
        )
        error = res.json()["errors"][0]["message"]
        assert 'Cannot query field "password"' in error
