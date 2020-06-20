from django.urls import path, re_path
from . import views

urlpatterns = [
	re_path(r'^$', views.home, name='index'),
	re_path(r'^get-bill$', views.get_bill, name='get_bill'),
]
