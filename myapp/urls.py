
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery/', views.mygallary, name='gallery'),
    path('about/', views.aboutus, name='about'),
    path('contact/', views.contactus, name='contact'),
    path('details/', views.details, name='details'),
    path('join/', views.join, name='join'),
]
