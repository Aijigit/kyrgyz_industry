from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('admin-panel/', views.admin_index_page, name='admin_panel'),
    path('admin-panel/add/', views.admin_form_page, name='forms_page')
]
