from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from homepage.views import user_logout, SignUpView

urlpatterns=[
    path('logout', user_logout, name='logout'),
    path('signup',SignUpView.as_view(), name ='signup'),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
