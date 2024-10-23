from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('new/<int:id>/', views.post_detail, name='post-detail'),
]