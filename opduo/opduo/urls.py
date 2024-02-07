from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('myapp.urls')),
    path('duo/', include('duo_universal_auth.urls')),
]
