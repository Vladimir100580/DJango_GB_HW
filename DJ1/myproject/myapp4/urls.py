from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import user_form, many_fields_form, add_user, upload_image, users, add_user_picture

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms', many_fields_form, name='many_fields_form'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
    path('users/', users, name='users'),
    path('add_user_picture/<int:user_id>/', add_user_picture, name='add_user_picture'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(f'{urlpatterns = }')
