from django.urls import path
from .views import home_page, register_page, login_page, logout_page, error_login, error_register, user_page, all_users_page, specific_user_page

urlpatterns = [
    path('', register_page, name = "register_page"),
    path('login/', login_page, name = "login_page"), # in html functions are looked from name argument name = "login_page"
    path('home/', home_page, name = 'home_page'),   
    path('logout/', logout_page, name = "logout_page"),
    path('error_register/', error_register, name = "error_register"),
    path('error_login/', error_login, name = "error_login"),
    path('user_page/', user_page, name = "user_page"),
    path('all_users_page/', all_users_page, name = "all_users_page"),
    path('specific_users_page/', specific_user_page, name = "specific_user_page")
    
]   