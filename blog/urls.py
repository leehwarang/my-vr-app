from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
     url(r'^$', views.post_all, name='post_all'),  # 이 url로 들어가면 post_all 라는 이름의 view가 보여짐.
    url(r'^spot/$', views.post_spot_list, name='post_spot_list'),
    url(r'^accomodation/$', views.post_accomodation_list, name='post_accomodation_list'),
    url(r'^restaurant/$', views.post_restaurant_list, name='post_restaurant_list'),
    url(r'^activity/$', views.post_activity_list, name='post_activity_list'),
    #url(r'^recreation/$', views.post_recreation_list, name='post_recreation_list'),
    url(r'^spot/(?P<pk>[0-9]+)/$', views.post_spot_detail, name='post_spot_detail'),
    url(r'^accomodation/(?P<pk>[0-9]+)/$', views.post_accomodation_detail, name='post_accomodation_detail'),
    url(r'^restaurant/(?P<pk>[0-9]+)/$', views.post_restaurant_detail, name='post_restaurant_detail'),
    #url(r'^recreation/(?P<pk>[0-9]+)/$', views.post_recreation_detail, name='post_recreation_detail'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^activity/new/$', views.post_activity_new, name='post_activity_new'),
    url(r'^spot/(?P<pk>\d+)/edit/$', views.post_spot_edit, name='post_spot_edit'),
    url(r'^accomodation/(?P<pk>\d+)/edit/$', views.post_accomodation_edit, name='post_accomodation_edit'),
    url(r'^restaurant/(?P<pk>\d+)/edit/$', views.post_restaurant_edit, name='post_restaurant_edit'),
    #url(r'^recreation/(?P<pk>\d+)/edit/$', views.post_recreation_edit, name='post_recreation_edit'),
    url(r'^spot/(?P<pk>[0-9]+)/delete/$', views.post_spot_delete, name='post_spot_delete'),
    url(r'^accomodation/(?P<pk>[0-9]+)/delete/$', views.post_accomodation_delete, name='post_accomodation_delete'),
    url(r'^restaurant/(?P<pk>[0-9]+)/delete/$', views.post_restaurant_delete, name='post_restaurant_delete'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),  # 아주 잘 작동됨
    url(r'^login/$', auth_views.login, {'template_name': 'blog/login.html'}), # 아주 잘 작동됨
    url(r'^like/$', views.post_like, name='post_like'),
    url(r'^spot/explore/tags/(?P<tag>\w+)/$', views.post_spot_list, name='post_spot_search'),
    url(r'^accomodation/explore/tags/(?P<tag>\w+)/$', views.post_accomodation_list, name='post_accomodation_search'),
    url(r'^restaurant/explore/tags/(?P<tag>\w+)/$', views.post_restaurant_list, name='post_restaurant_search'),
]

