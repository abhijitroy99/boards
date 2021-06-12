from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('', include('boards.urls')),  
    path('', include('accounts.urls')),  
    #path(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
    
    
]   

    