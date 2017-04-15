from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

#app_name = 'snippet'

urlpatterns = [
    url(r'^$', views.api_root, name='api-root'),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>\d+)$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'snippet/(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)', views.UserDetail.as_view(), name='user-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)