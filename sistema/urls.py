from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^$', Welcome.as_view(), name="home")
]