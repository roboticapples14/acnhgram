from django.urls import path
from . import views


urlpatterns= [
  path('', views.showcase.as_view(), name='showcase'),
  path('post_edit/', views.post_new, name='post_new'),
]