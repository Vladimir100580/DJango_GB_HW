
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gb_app4.urls')),
    path('les3/', include('gb_app3.urls')),
    # path('__debug__/', include("debug_toolbar.urls")),
]

# path('admin/', admin.site.urls),
# path('prefix/', include('myapp.urls')),
# path('les3/', include('myapp3.urls')),  # здесь '/' обязателен
# path('', index),
# path('les4/', include('myapp4.urls')),