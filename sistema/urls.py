from django.conf.urls import include, url
from .views import *

app_name = 'sistema'
urlpatterns = [
	url(r'^$', Welcome.as_view(), name="home")
]
