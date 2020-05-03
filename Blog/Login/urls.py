from django.urls import path

from Login.views import PostListView
from . import views

app_name = 'Login'

urlpatterns = [
    path('', views.user_login, name='index'),
    path('home', PostListView.as_view(), name='home'),
    path('register', views.user_register, name='register'),
    path('about', views.AboutView.as_view(), name='about'),
    path('add_post', views.PostCreateView.as_view(), name='add_post'),
    path('delete/<pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('update/<pk>/', views.PostUpdateView.as_view(), name='update'),
    path('add_comment/<pk>', views.add_comment, name='add_comment'),
    path('view_comment/<pk>', views.PostDetailView.as_view(), name='view_comment'),
    path('update_comment/<pk>', views.CommentUpdateView.as_view(), name='update_comment'),
    path('delete_comment/<pk>', views.CommentDeleteView.as_view(), name='delete_comment'),

]
