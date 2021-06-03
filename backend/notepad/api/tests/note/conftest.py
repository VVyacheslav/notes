import pytest
from django.urls import reverse

from notepad.tests.factories import NoteFactory


@pytest.fixture
def note():
    return NoteFactory()


@pytest.fixture
def url(note):
    return reverse('v1:notepad:note-detail', args=[note.id])


@pytest.fixture
def list_url():
    return reverse('v1:notepad:note-list')
