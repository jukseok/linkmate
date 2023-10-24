from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookmarkList.as_view()),
    path('<int:pk>/', views.BookmarkDetail.as_view()),
    path('update_bookmark/<int:pk>/', views.BookmarkUpdate.as_view(), name='update_bookmark'),
    path('delete_bookmark/<int:pk>/', views.BookmarkDelete.as_view(), name='delete_bookmark'),
    path('tag/<str:slug>/', views.tag_page),
    path('create_bookmark/', views.BookmarkCreate.as_view()),
    path('search/<str:q>/', views.BookmarkSearch.as_view(), name='bookmark_search'),
    path('manage_tags/', views.ManageTags.as_view(), name='manage_tags'),
    path('tags/create/', views.TagCreate.as_view(), name='tag_create'),
    path('tags/detail/<str:slug>/', views.TagDetail.as_view(), name='tag_detail'),
    path('tags/delete/<str:slug>/', views.TagDelete.as_view(), name='tag_delete'),

    
]

