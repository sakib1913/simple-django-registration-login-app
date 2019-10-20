from django.urls import path
from . import views
urlpatterns=[  
  path('index/',views.indexView,name="home"),
  path('register/',views.registerView,name="register.url"),
  
]