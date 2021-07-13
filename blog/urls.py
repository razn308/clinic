from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.CreateBlogView, name='create_post'),
    path('details/', views.BlogDetailView, name='detail_post'),
]
