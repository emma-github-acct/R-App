from django.conf.urls import include, url
from django.contrib import admin
from display import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^location/(?P<id>\d+)/', views.location_detail, name='location_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
