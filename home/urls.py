from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^open-new-page/(?P<unique_id>[\w-]+)/$', views.new_page, name='new_page'),
    url(r'^edit-wiki-object/(?P<unique_id>[\w-]+)/$', views.edit_wiki_object, name='edit_wiki_object'),
    url(r'^search', views.search, name='search'), 
    url(r'^$', views.home, name='home'), 
]


