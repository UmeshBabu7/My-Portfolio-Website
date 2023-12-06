from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('Login/',views.handleLogin,name='handleLogin'),
    path('Logout/',views.handleLogout,name='handleLogout'),
]
