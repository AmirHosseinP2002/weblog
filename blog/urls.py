from django.urls import path

from . import views

urlpatterns = [
    # path('', views.posts_list_view, name='posts_list'),
    path('', views.PostListView.as_view(), name='posts_list'),
    # path('<int:pk>/', views.post_detail_view, name='post_detail'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('create/', views.post_create_view, name='post_create'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    # path('<int:pk>/update/', views.post_update_view, name='post_update'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    # path('<int:pk>/delete/', views.post_delete_view, name='post_delete'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
