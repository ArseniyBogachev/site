from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/', Category_list.as_view(), name='category'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('about/', About.as_view(), name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('user/', UserInfo.as_view(), name='user'),
    path('logout/', logout_user, name='logout'),
    path('category/<slug:cat_slug>/', Cosmos.as_view(), name='cosmos'),
    path('category/info/<slug:cos_slug>/', Show_post.as_view(), name='info'),
]