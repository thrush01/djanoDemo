from django.contrib.auth import views as auth_views
from django.urls import path

from .import views

from .forms import LoginForm

app_name='pool'
urlpatterns = [

    path('',views.index,name='index'),
    path('content/',views.content,name='content'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='demo/login.html',authentication_form=LoginForm),name='login'),
]
