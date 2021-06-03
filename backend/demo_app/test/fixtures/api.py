import pytest
from django.contrib.auth.models import AnonymousUser

from demo_app.test.api_client import DRFClient


@pytest.fixture
def api():
    return DRFClient()


@pytest.fixture
def api_factory():
    def _as_user(user=None, **kwargs):
        return DRFClient(user, **kwargs)

    return _as_user


@pytest.fixture
def as_user(api_factory, user):
    return api_factory(user)


@pytest.fixture
def as_another_user(api_factory, another_user):
    return api_factory(another_user)


@pytest.fixture
def as_anonymous(api_factory):
    user = AnonymousUser()
    return api_factory(user)


@pytest.fixture
def as_staff(api_factory, staff):
    return api_factory(staff)


@pytest.fixture
def as_superuser(api_factory, superuser):
    return api_factory(superuser)
