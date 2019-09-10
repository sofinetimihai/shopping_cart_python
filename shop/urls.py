from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'', views.product_list, name='product_list'),
    url(r'^category/(?P<categoryid>\d+)/$', views.product_list_by_category, name='product_list_by_category'),
    url(r'^produs/(?P<id>\d+)/$', views.product_detail, name='product_detail'),
    #re_path(r'^.*$', views.home),
    ]
