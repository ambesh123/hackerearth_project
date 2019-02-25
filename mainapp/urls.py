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
    path('sortbyprice/', views.sortbyprice),
    path('sortbypoints/', views.sortbypoints),
    path('getdesc/', views.getDesc),
    path('search/', views.search),
    path('logout/' , views.logout)
]
