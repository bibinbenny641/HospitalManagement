from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_login,name='adminlogin'),
    path('adminhome/',views.admin_home,name='adminhome'),
    path('logoutadmin/',views.logoutadmin,name='logoutadmin'),
    path('addHeadUser/',views.addHeadUser,name='addHeadUser'),
    path('deleteHeaduser/<id>/',views.deleteHeaduser,name='deleteHeaduser'),
    path('changepassword/',views.changepassword,name='changepassword'),
    # path('editHeaduser/<id>/',views.editHeaduser,name='editHeaduser'),


]