from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import get_object_or_404
from django.db.models.deletion import RestrictedError
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


""" 
    Таски:
        Client:
            Вывод Новостей
            Архив новостей
            Вывод Проекта
            Вывод Конкурса
            Вывод Вакансии
            Вывод Структуры
            Страницы для Детально
            Создать страницу для Галереи
            Создать карту сайта
            Обратная связь
            Страница для вакансии и вывод активных вакансии
            
        Админ:
            Страница авторизации
            CRUD Операции - Для Новостей
            CRUD Операции - Для Галерея-Новости
            CRUD Операции - Для Изображения-Новости
            
            CRUD Операции - Для Проекта
            CRUD Операции - Для Галерея-Проект
            CRUD Операции - Для Изображения-Новости
            
            CRUD Операции - Для Конкурса
            CRUD Операции - Для Галерея-Конкурс
            CRUD Операции - Для Изображения-Конкурс
            
            Создать - Модель Сотрудники
            Создать - Модель Вакансии
"""
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
    paginate_by = 10
    
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
    login_url = 'login_page'
    success_url = reverse_lazy("news_all")
    template_name = "admin/pages/news/news-edit.html"
    success_message = "Запись успешно обновлена!"
        
           
def news_delete(request, id):
    context = {}
    obj = get_object_or_404(News, id = id)
    if request.method =="POST":
        
        try:
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("news_all")
        except Exception as e:
            messages.error(request, "Не удалось удалить запись, повторите попытку!")
            return redirect("news_all")
 
    return render(request, "admin/pages/news/news_delete.html", context)

class NewsDetailView(LoginRequiredMixin, SuccessMessageMixin, NewsView, DetailView):
    login_url = "login_page"
    template_name = "admin/pages/news/news-detail.html"
"""
---- News-Gallery Views
"""
class NewsGalleryView(View):
    model = GalleryNews
    fields = '__all__'
    form_class = NewsGalleryForm
    extra_context = {
        "is_active" : "gallery-panel",
        "active_gallery_news" : "active",
        "expand_gallery" : "show",
        }

class NewsGalleryListView(LoginRequiredMixin, NewsGalleryView, ListView):
    login_url = 'login_page'
    template_name = 'admin/pages/news-gallery/newsgallery_list.html'
    paginate_by = 10

class NewsGalleryCreateView(LoginRequiredMixin, NewsGalleryView, CreateView):
    login_url = 'login_page'
    template_name = 'admin/pages/news-gallery/newsgallery_form.html'
    redirect_field_name = "newsgallery_create"
    def get(self, request, *args, **kwargs):
        
        form = NewsGalleryForm()
        context = {
            "form" : form,
            "is_active" : "gallery-panel",
            "expand_gallery" : "show",
            "active_create_gallerynews" : "active"
            
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = NewsGalleryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(self.redirect_field_name)
            else:
                return redirect(self.redirect_field_name)
        else:
            messages.error(request, "Invalid Method")
            return redirect(self.redirect_field_name) 

class NewsGalleryUpdateView(LoginRequiredMixin, NewsGalleryView, DeleteView):
    template_name = 'admin/pages/news-gallery/newsgallery_form.html'
    success_url = reverse_lazy("newsgallery_all")
    success_message = "Запись успешно обновлено!"      
    
def newsgallery_delete(request, id):
    context = {}
    obj = get_object_or_404(GalleryNews, id = id)
    if request.method =="POST":
        try:
        # delete object
            obj.delete()
        # after deleting redirect to
        # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("newsgallery_all")
        except RestrictedError:
            messages.error(request, "Вы не сможете удалить эту галерею, так как это связано с одной или несколькими новостями или фотографиями")
            return redirect("newsgallery_all")
    return render(request, "admin/pages/news-gallery/newsgallery_confirm_delete.html", context)

"""
---- End News-Gallery Views
"""
"""
---- News-Image Views
"""
class NewsImageView(View):
    model = PhotosNews
    fields = '__all__'
    form_class = NewsImageForm
    success_url = reverse_lazy("newsimage_all")
    extra_context = {
        "is_active" : "gallery-panel",
        "active_gallery_news" : "active",
        "expand" : "show",
        }
class NewsImageListView(LoginRequiredMixin, NewsImageView, ListView):
    template_name = 'admin/pages/news-image/newsgallery_list.html'
    paginate_by = 10

class NewsImageCreateView(LoginRequiredMixin, NewsImageView, CreateView):
    template_name = 'admin/pages/news-gallery/newsgallery_form.html'
    redirect_field_name = "newsgallery_create"
    def get(self, request, *args, **kwargs):
        
        form = NewsImageForm()
        context = {
            "form" : form,
            "is_active" : "gallery-panel",
            "expand" : "show",
            "active_create_gallerynews" : "active"
            
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = NewsGalleryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(self.redirect_field_name)
            else:
                return redirect(self.redirect_field_name)
        else:
            messages.error(request, "Invalid Method")
            return redirect(self.redirect_field_name) 

class NewsImageUpdateView(LoginRequiredMixin, NewsImageView, DeleteView):
    template_name = 'admin/pages/news-gallery/newsgallery_form.html'
    success_message = "Запись успешно обновлено!"      
    
class NewsGalleryDeleteView(LoginRequiredMixin, NewsGalleryView, DeleteView):
    template_name = 'admin/pages/news-gallery/newsgallery_confirm_delete.html'
    success_url = reverse_lazy("newsgallery_all")
    success_message = "Запись успешно удалено!"

"""
---- End News-Image Views
"""    