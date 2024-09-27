from django.urls import path

from .views import Home_Page_View
from .views import Second_Function_View

urlpatterns=[
    path('', Home_Page_View, name='home'),
    path('about/',Second_Function_View,name='second_function'),
]