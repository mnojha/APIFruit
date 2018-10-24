from django.urls import path
#from api.views import fruit_list

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import CreateView


urlpatterns = [
#	path('fruit_list', fruit_list, name = "fruit_list"),
	path('', CreateView.as_view(), name="create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)