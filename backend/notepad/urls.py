from django.urls import include, path
from rest_framework.routers import SimpleRouter

from notepad.api.views import NoteViewSet

router = SimpleRouter()
router.register('notes', NoteViewSet)

app_name = 'notepad'
urlpatterns = [
    path('', include(router.urls)),
]
