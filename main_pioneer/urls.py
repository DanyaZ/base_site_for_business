from django.urls import path, include
from django.contrib.auth import views as views_auth
from . import views

urlpatterns = [
    path('',views.Main.as_view(), name='main'),
    path('about_us',views.AboutUs.as_view(), name='about_us'),
    path('services',views.Services.as_view(), name='services'),
    path('blog',views.Blog.as_view(), name='blog'),
    path('contacts',views.Contacts.as_view(), name='contacts'),
    path('team',views.Team.as_view(), name='team'),
    path('historis',views.History.as_view(), name='historis'),
    path('login/', views_auth.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add_blog',views.AddBlog.as_view(), name='add_blog'),
    path('<slug:slug>new',views.NewShow.as_view(), name='article')

]
