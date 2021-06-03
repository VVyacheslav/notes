from django.contrib import admin
from django.urls import path, include

app_name = 'api_v1'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notepad/', include('notepad.urls', namespace='notepad')),
]
