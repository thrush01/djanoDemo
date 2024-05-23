
from django.contrib import admin
from django.urls import path
from POLL.views import index,content

urlpatterns = [
    path('',index,name='index'),
    path('content/',content,name='content'),
    path('admin/', admin.site.urls),
]
