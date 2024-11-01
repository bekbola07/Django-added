from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),
    path('all-news',all_news, name='all_news'),
    path('detail/<int:pk>', Detail_page.as_view(), name='detail')
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)