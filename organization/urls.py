from django.conf.urls import url
from . import views

app_name = "organization"
urlpatterns = [
    # ex: /organization/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /organization/71/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /organization/organization/add/
    url(r'^organization/add/$', views.OrganizationCreate.as_view(), name='organization-add'),
    # /organization/organization/2/
    url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationUpdate.as_view(), name='organization-update'),
    # /organization/organization/2/delete/
    url(r'^organization/(?P<pk>[0-9]+)/delete/$', views.OrganizationDelete.as_view(), name='organization-delete'),
]
