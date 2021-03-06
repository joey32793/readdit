from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^create_post/', views.create_post, name="create_post"),
    url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
    url(r'^posts_by_user/(?P<fk>[0-9]+)', views.posts_by_user, name="posts_by_user"),
    url(r'^user_post/(?P<fk>[0-9]+)', views.user_post, name="user_post"),
]
