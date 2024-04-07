from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name="home"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('register',views.register,name="register"),
    path('places',views.places,name="places"),
    path('places/<str:name>',views.placesview,name="places"),
    path('places/<str:cname>/<str:pname>',views.product_details,name="product_details")


]