import pytest

from notepad.models.note import Note

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def post_data():
    return {
        'content': 'Some content',
    }


def test_create_tournament_note(list_url, as_anonymous, post_data):
    resp = as_anonymous.post(list_url, post_data)

    note = Note.objects.get(id=resp['id'])
    assert note.content == post_data['content']
