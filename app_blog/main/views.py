from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import *


def index(request):
    template_name = "client/index.html"
    return render(request, template_name, {})


def detail(request):
    template_name = "client/pages/blog_detail.html"
    return render(request, template_name, {})


# Admin-Panel Views
def admin_index_page(request):
    template_name = "admin/admin.html"
    context = {
        "is_active" : "main-panel"
    }
    return render(request, template_name, context)

def admin_form_page(request):
    template_name = "admin/pages/forms/basic_elements.html"

    user_name = None
    if request.user.is_authenticated:
        user_name = request.user.username
    context = {
        "user" : user_name
    }
    return render(request, template_name, context)


def login_page(request):
    template_name = "admin/pages/forms/login.html"

    return render(request, template_name, {})

class NewsView(View):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('news_all')
    extra_context = {
        "is_active" : "news-panel",
        "expand" : "show"
        }

class NewsListView(LoginRequiredMixin, NewsView, ListView):
    login_url = 'login_page'
    template_name = 'admin/pages/news/news-all.html'
    

  