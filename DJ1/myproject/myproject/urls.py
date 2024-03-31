from myapp3.views import index
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('myapp.urls')),
    path('les3/', include('myapp3.urls')),   # здесь '/' обязателен
    path('', index)
    ]
