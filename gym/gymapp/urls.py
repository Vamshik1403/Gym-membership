from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path("home/",views.home),
    path("bmi/",views.bmi),
    path("foot/",views.fo),
    path("head/",views.hd),
    path("pricing",views.price),
    path("product",views.product),
    path("program",views.prog),
    path("profile/",views.profile),
    path("login/",views.user_login),
    path("logout/",views.user_logout),
    path("register/",views.user_register),
    path('pay/',views.pay),
    path("productdetails/<pid>/",views.productdetails),
    path("addtocart/<pid>",views.addToCart),
    path("enroll/",views.enrollment)
]



