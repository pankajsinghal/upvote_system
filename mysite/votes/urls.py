from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /votes/
    url(r'^$', views.index, name='index'),
    # ex: /votes/5/upvote/
    url(r'^(?P<question_id>[0-9]+)/upvote/$', views.upvote, name='upvote'),
    # ex: /votes/5/downvote/
    url(r'^(?P<question_id>[0-9]+)/downvote/$', views.downvote, name='downvote'),
]
