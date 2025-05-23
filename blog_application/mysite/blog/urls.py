from django.urls import re_path
from blog import views

urlpatterns = [
    re_path(r"^$", views.PostListView.as_view(), name="post_list"),
    re_path(r"^about/$", views.AboutView.as_view(), name="about"),
    re_path(r"^post/(?P<pk>\d+)$", views.PostDetailView.as_view(), name="post_detail"),
    re_path(r"^post/new/$", views.CreatePostView.as_view(), name="post_new"),
    re_path(r"^post/(?P<pk>\d+)/edit/$", views.PostUpdateView.as_view(), name="post_edit"),
    re_path(
        r"^post/(?P<pk>\d+)/remove/$",
        views.PostDeleteView.as_view(),
        name="post_remove",
    ),
    re_path(r"^drafts/$", views.DraftListView.as_view(), name="post_draft_list"),
    re_path(
        r"^post/(?P<pk>\d+)/comment/$",
        views.add_comment_to_post,
        name="add_comment_to_post",
    ),
    re_path(
        r"^comment/(?P<pk>\d+)/approve/$", views.comment_approve, name="comment_approve"
    ),
    re_path(r"^comment/(?P<pk>\d+)/remove/$", views.comment_remove, name="comment_remove"),
    re_path(r"^post/(?P<pk>\d+)/publish/$", views.post_publish, name="post_publish"),
]
