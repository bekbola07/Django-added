from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls'), name='posts'),
    path('account/', include('django.contrib.auth.urls')),
    path('accounts', include('accounts.urls')),
 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
