from django.urls import path , re_path, include
from mainapp import views

urlpatterns = [
    path('' , views.index),
    path('signup/' , views.signUp),
    path('login/' , views.login),
    path('home/' , views.home),
    path('upload_csv/', views.upload_csv),
    path('import_csv/', views.import_csv),
    path('adduser/' , views.addUser),
    path('home/sortbyprice/', views.sortbyprice),
    path('home/sortbypoints/', views.sortbypoints),
    path('home/getdesc/', views.getDesc),
    path('logout/' , views.logout)
]
