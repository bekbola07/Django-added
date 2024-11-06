from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import category, region, all_region, all_category, CreatePost, all_news, home, detail

urlpatterns=[
    path('', home, name='home'),
    path('all-news', all_news, name='all_news'),
    path('category/<int:id>', category, name='category'),
    path('all-categories', all_category, name='all-category'),
    path('region/<int:id>', region, name='region'),
    path('all-regions', all_region, name='all-region'),
    path('create-post/new', CreatePost.as_view(), name='create_post'),
    path('detail/<int:id>', detail, name='detail'),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
