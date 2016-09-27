from django.conf.urls import url
from . import views
#from django.contrib import admin

urlpatterns = [
	url(r'^create$', views.create),
	url(r'^process$', views.process),
	url(r'^(?P<id>\d+)$', views.viewproduct),
	
]