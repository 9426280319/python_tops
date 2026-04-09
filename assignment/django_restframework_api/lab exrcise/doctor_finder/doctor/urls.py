from django.urls import path
from doctor import views

urlpatterns = [
    path('', views.home),
    path('doctors/', views.doctor_list),
    path('add/', views.add_doctor),
    path('update/<int:id>/', views.update_doctor),  
    path('delete/<int:id>/', views.delete_doctor),  
    path('register/', views.register),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
]