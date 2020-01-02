from django.urls import path
from authr import views

app_name = 'authr'

urlpatterns = [
    path(r'^register/$',views.register,name='register'),
    path(r'^user_login/$',views.user_login,name='user_login')

]
