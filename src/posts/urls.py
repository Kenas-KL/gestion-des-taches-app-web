from django.contrib.auth import views as auth_views, views
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from .views import TachesHome, TachesCreate, TachesUpdate, TachesDetail, TachesDelete, signup, logout_view
from django.contrib.auth.decorators import login_required

app_name = "posts"


urlpatterns = [
    path('', signup, name="signup"),
    path('login/home/', login_required(TachesHome.as_view()), name="acceuil"),
    path("login/", LoginView.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
    path('add/', login_required(TachesCreate.as_view()), name="add"),
    path('<str:pk>/', login_required(TachesDetail.as_view()), name="post"),
    path('edit/<str:pk>/', login_required(TachesUpdate.as_view()), name="edit"),
    path('delete/<str:pk>/', login_required(TachesDelete.as_view()), name="delete")
]

