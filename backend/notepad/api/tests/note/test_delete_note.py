import pytest

from notepad.models.note import Note

pytestmark = [pytest.mark.django_db]


def test_delete_tournament_role_by(url, as_anonymous, note):
    as_anonymous.delete(url)

    assert not Note.objects.filter(id=note.id).exists()

