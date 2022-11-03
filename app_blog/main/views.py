from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import *
from .forms import *

from django.contrib.auth.backends import UserModel
def index(request):
    template_name = "client/index.html"
    return render(request, template_name, {})


def detail(request):
    template_name = "client/pages/blog_detail.html"
    return render(request, template_name, {})

@csrf_exempt
def login_page(request):
    success_url = reverse_lazy('admin_panel')
    template_name = "admin/pages/forms/login.html"
    if request.user.is_authenticated:
        return redirect(success_url)
    else:
        return render(request, template_name, {})


@csrf_exempt
def authorization(request):
    success_url = reverse_lazy('admin_panel')
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    try:
        account = authenticate(username=UserModel.objects.get(email=username).username, password=password)
        if account is not None and request.method == 'POST':
            login(request, account)
            return redirect(success_url)
        else:
            messages.error(request, "Логин или пароль неправильно")
            return redirect('login_page')
    except:
        if username == "":
            messages.error(request, "Введите ваш Логин или E-mail")
            return redirect('login_page')
        elif password == "":
            messages.error(request, "Введите пароль")
            return redirect('login_page')
        else:
            account = authenticate(username=username, password=password)
            if account is not None and request.method == 'POST':
                login(request, account)
                return redirect(success_url)
            else:
                messages.error(request, "Логин или пароль неправильно")
                return redirect('login_page')
   

def logout_page(request):
    logout(request)
    return redirect('login_page')

# Admin-Panel Views
@login_required
def admin_index_page(request):
    template_name = "admin/admin.html"
    context = {
        "is_active" : "main-panel"
    }
    return render(request, template_name, context)

@login_required
def admin_form_page(request):
    template_name = "admin/pages/forms/basic_elements.html"

    user_name = None
    if request.user.is_authenticated:
        user_name = request.user.username
    context = {
        "user" : user_name
    }
    return render(request, template_name, context)




class NewsView(View):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('news_all')
    extra_context = {
        "is_active" : "news-panel",
        "active_all_news" : "active",
        "expand" : "show",
        }

class NewsListView(LoginRequiredMixin, NewsView, ListView):
    login_url = 'login_page'
    template_name = 'admin/pages/news/news-all.html'
    
class NewsCreateView(LoginRequiredMixin, NewsView, CreateView):
    login_url = 'login_page'
    template_name = 'admin/pages/news/news-add.html'
    redirect_field_name = "news_create"
    def get(self, request, *args, **kwargs):
        
        form = NewsForm()
        context = {
            "form" : form,
            "is_active" : "news-panel",
            "expand" : "show",
            "active_create_news" : "active"
            
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = NewsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(self.redirect_field_name)
            else:
                return redirect(self.redirect_field_name)
        else:
            messages.error(request, "Invalid Method")
            return redirect(self.redirect_field_name) 

class NewsUpdateView(LoginRequiredMixin,SuccessMessageMixin, NewsView, UpdateView):
    model = News
    login_url = 'login_page'
    success_url = reverse_lazy("news_all")
    template_name = "admin/pages/news/news-edit.html"
    success_message = "Успешно изменено"
            
class NewsDeleteView(LoginRequiredMixin,SuccessMessageMixin, NewsView, DeleteView):
    login_url = 'login_page'
    template_name = "admin/pages/news/news-delete.html"
    model = News
    success_url = reverse_lazy("news_delete")
    success_message = "Успешно удалено"
   