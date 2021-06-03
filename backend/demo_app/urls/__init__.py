from django.contrib import admin
from django.urls import include, path

api = [
    path('v1/', include('demo_app.urls.v1', namespace='v1')),
]

urlpatterns = [
    path('api/', include(api)),
    path('admin/', admin.site.urls),
]
