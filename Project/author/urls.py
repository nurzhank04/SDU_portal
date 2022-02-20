
from django.urls import path, re_path
from . views import *

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
] 