import pytest

pytestmark = [pytest.mark.django_db]


def get_note_expected_data(note):
    return {
        'id': note.id,
        'content': note.content,
    }



def test_list_notes(as_anonymous, list_url, note):
    got = as_anonymous.get(list_url)

    assert len(got['results']) == 1
    role_data = got['results'][0]

    assert role_data == get_note_expected_data(note)


def test_retrieve_note(as_anonymous, url, note):
    data = as_anonymous.get(url)
    assert data == get_note_expected_data(note)
