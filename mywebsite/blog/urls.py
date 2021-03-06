from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('comment/', views.comment_list, name='comment_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]