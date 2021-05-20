from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('signup/', sign_up, name = 'sign_up'),
    path('login/', login_page, name='login'),
    path('logout', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('change-profile', user_change, name = 'change_profile'),
    path('password/', pass_change, name='change_password'),
    path('add-picture/', add_pro_pic, name='add_picture')
    
]
