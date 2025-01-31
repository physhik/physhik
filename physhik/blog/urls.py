from django.urls import path, include
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('',
         TemplateView.as_view(template_name='blog/index.html'),
         name="home"),

    path('postlist', views.GenericPostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.GenericPostDetailView.as_view(), name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts', views.GenericPostDraftView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/',
         views.add_comment_to_post,
         name='add_comment_to_post'),



    path('comment/<int:pk>/approve/',
         views.comment_approve,
         name='comment_approve'),
    path('comment/<int:pk>/remove/',
         views.comment_remove,
         name='comment_remove'),

     path('tracker',
         TemplateView.as_view(template_name='blog/tracker.html'),
         name="tracker"),
    path('ecg',
         TemplateView.as_view(template_name='blog/ecg.html'),
         name="ecg"),
    path('mlbplayers',
         TemplateView.as_view(template_name='blog/mlbplayers.html'),
         name="mlbplayers"),
    path('cluster_mlb',
         TemplateView.as_view(template_name='blog/cluster_mlb.html'),
         name="cluster_mlb"),
    path('progress',
         TemplateView.as_view(template_name='blog/progress.html'),
         name="progress"),
]
