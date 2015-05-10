from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /votes/
    url(r'^$', views.index, name='index'),
    # ex: /votes/5/upvote/
    url(r'^(?P<photo_id>[0-9]+)/upvote/$', views.upvote, name='upvote'),
    # ex: /votes/5/remove_upvote/
    url(r'^(?P<photo_id>[0-9]+)/remove_upvote/$', views.remove_upvote, name='remove_upvote'),
    # ex: /votes/5/downvote/
    url(r'^(?P<photo_id>[0-9]+)/downvote/$', views.downvote, name='downvote'),
    # ex: /votes/5/remove_downvote/
    url(r'^(?P<photo_id>[0-9]+)/remove_downvote/$', views.remove_downvote, name='remove_downvote'),
]
