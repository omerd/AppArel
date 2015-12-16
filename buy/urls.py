from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_handler, name='login'),
	url(r'^logged/$', views.logged, name='logged_view'),
    url(r'^reg$', views.reg, name='reg'),
    url(r'^pay/$', views.pay, name='pay'),
	url(r'^details/(?P<id>[0-9]+)/$', views.getProductDetails, name='details'),
]