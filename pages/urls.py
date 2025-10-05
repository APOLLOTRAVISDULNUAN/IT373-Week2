
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('gallery/', views.gallery, name='gallery'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('announcements/<int:id>/', views.announcement_detail, name='announcement_detail'),
]
