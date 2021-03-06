from django.urls import path, re_path
from django.conf.urls import url
#from home.views import index
import home
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import CreateView, DeleteUserView, CategoryView, DeleteCategoryView
from .views import *



urlpatterns = [
        re_path(r'^$', home.views.index, name='index'),
        url(r'^v1/users/$', CreateView.as_view(), name="create"),
        url(r'^v1/users/(?P<pk>[0-9]+)/$', DeleteUserView.as_view(), name="details"),
        url(r'^v1/categories/$', CategoryView.as_view(), name="createCategory"),
        url(r'^v1/categories/(?P<pk>[0-9]+)/$', DeleteCategoryView.as_view(), name="detailsCategory"),

        url(r'^v1/acts/$', PostView.as_view(), name="createPost"),
        url(r'^v1/acts/(?P<pk>[0-9]+)/$', DeletePostView.as_view(), name="detailsPost"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
