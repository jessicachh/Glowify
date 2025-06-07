# accounts/urls.py
from django.urls import path
from . import views
from .views import blog_view 

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('skintype/', views.skintype, name='skintype'),
    path('skincare/', views.skincare, name='skincare'),
    path('products/', views.products, name='products'),
    path('blog/', blog_view, name='blog'),
    path('blog/edit/<int:post_id>/', views.edit_blog_post, name='edit-blog-post'), 
    path('blog/delete/<int:post_id>/', views.delete_blog_post, name='delete-blog-post'), 
]
