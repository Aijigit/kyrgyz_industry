from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login_page, name='login_page'),
    path('accounts/login/success/', views.authorization, name='authorizate'),
    path('accounts/logout/', views.logout_page, name = 'logout_page'),
    path('detail/', views.detail, name='detail'),
    path('admin-panel/admin-main/', views.admin_index_page, name='admin_panel'),
    path('admin-panel/add/', views.admin_form_page, name='forms_page'),
    path('admin-panel/news/all/', views.NewsListView.as_view(), name='news_all'),
]
