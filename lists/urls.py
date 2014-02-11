from django.conf.urls import patterns, include, url

urlpatterns = patterns('lists.views',
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^new$', 'new_list', name='new_list'),
    url(r'^(?P<list_id>\d+)/$', 'view_list', name='view_list'),
    url(r'^(?P<list_id>\d+)/new_item$', 'add_item', name='add_item'),
)
