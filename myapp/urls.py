from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogOut,name='logout'),
    path('add/',views.AddStudent,name='add'),
    path('view/',views.ViewStudent,name='view'),
    path('search/',views.Search,name='search'),
    path('delete/<int:id>/',views.DeleteStudent,name='delete'),
]