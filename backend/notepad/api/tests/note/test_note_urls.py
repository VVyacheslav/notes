import pytest

pytestmark = [pytest.mark.django_db]


def test_list_url(list_url):
    assert list_url == '/api/v1/notepad/notes/'
