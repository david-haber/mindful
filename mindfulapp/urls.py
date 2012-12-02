from django.conf.urls import patterns, include, url
from mindfulapp import views

urlpatterns = patterns('',
	url(r'^$', views.landing, name="landing"),
	url(r'^user/(?P<id>\d+)/play$', views.user_play, name="user_play"),
	url(r'^carer/(?P<id>\d+)$', views.carer, name="carer"),
	url(r'^$', views.index, name='index'),
	url(r'^login$', views.login_user, name="login_user"),
	url(r'^login-carer$', views.login_carer, name="login_carer"),
	url(r'^logout$', views.logout, name="logout")
)
