from authr import views
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^admin/',admin.site.urls),
    url(r'^authisation/',include('authr.urls')),
    url(r'^logout/',views.user_logout,name='logout')

]
