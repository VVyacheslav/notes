import pytest

pytestmark = [pytest.mark.django_db]


def test_update_tournament_bleach_rules_and_description(url, as_anonymous, note):
    as_anonymous.put(url, {
        'content': 'New content',
    })

    note.refresh_from_db()
    assert note.content == 'New content'
