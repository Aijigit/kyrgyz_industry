<<<<<<< HEAD
from django.contrib import messages
=======
import os
>>>>>>> 69018b9ef27a8f551a156c7e22d9e6dc2aaccc86
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
<<<<<<< HEAD
from django.core.mail import BadHeaderError, send_mail
from django.core import mail
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
=======
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
>>>>>>> 69018b9ef27a8f551a156c7e22d9e6dc2aaccc86
def index(request):
   
    
    template_name = "client/index.html"
    return render(request, template_name, {})

def send_message(request):
    
    sucs=True
    if request.method == 'POST':
        settings.EMAIL_HOST_USER=request.POST.get('email', '')
        settings.EMAIL_HOST_PASSWORD=''
        Name = request.POST.get('name', '')
        
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')
        subject = "Сообщение от пользователей" 
        try:
            
            body = {
			    'Name: ': "От кого: "+ Name, 
                'from_email': "Эл.адрес: " + from_email,
			    'message': "Сообщение: " + message,
		    }
	    
            messageAll = "\n".join(body.values())
            send_mail(subject, messageAll, from_email, ['To'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except:
            messages.add_message(request, messages.ERROR, 'Неправильный эл.адрес')
            sucs=False
    if(sucs==True):
        messages.add_message(request, messages.SUCCESS, 'Ваше сообщение отправлено!')
    return redirect ('/')


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
        "active_news" : "active",
        "expand_news" : "show",
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
            "expand_news" : "show",
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
    form_class = NewsGalleryForm
    extra_context = {
        "is_active" : "news-panel",
        "active_news_gallery" : "active",
        "expand_news" : "show",
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
            "is_active" : "news-panel",
            "expand_news" : "show",
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = NewsGalleryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Запись Успешно добавлено!")
                return redirect(self.redirect_field_name)
            else:
                messages.error(request, "Введите корректные данные!!")
                return redirect(self.redirect_field_name)
        else:
            messages.error(request, "Invalid Method")
            return redirect(self.redirect_field_name) 

class NewsGalleryUpdateView(LoginRequiredMixin, SuccessMessageMixin, NewsGalleryView, UpdateView):
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
    form_class = NewsImageForm
    success_url = reverse_lazy("newsimage_all")
    login_url = "login_page"
    extra_context = {
        "is_active" : "news-panel",
        "active_news_image" : "active",
        "expand_news" : "show",
        }
class NewsImageListView(LoginRequiredMixin, NewsImageView, ListView):
    template_name = 'admin/pages/news-image/newsimage_list.html'
    paginate_by = 10
    

<<<<<<< HEAD
def ProjectsGetAll(request):
    projects = Projects.objects.all()
    return render(request, 'client/index.html', {'project':projects})
=======
class NewsImageCreateView(LoginRequiredMixin, NewsImageView, CreateView):
    template_name = 'admin/pages/news-image/newsimage_form.html'
    redirect_field_name = "newsimage_create"
    def get(self, request, *args, **kwargs):
        form = NewsImageForm()
        context = {
            "form" : form,
            "is_active" : "news-panel",
            "expand_news" : "show",
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = NewsImageForm(request.POST, request.FILES)
            try:
                form.save()
                messages.success(request, "Изображение Успешно добавлено!")
                return redirect(self.redirect_field_name)
            except ValueError:
                messages.error(request, "Выберите картинку в формате (jpg, jpeg, png, и т.д.)")
                return redirect(self.redirect_field_name)
            except Exception as e:
                messages.error(request, e)
                return redirect(self.redirect_field_name)
        else:
            messages.error(request, "Invalid Method")
            return redirect(self.redirect_field_name) 

class NewsImageUpdateView(LoginRequiredMixin, NewsImageView, UpdateView):
    template_name = 'admin/pages/news-image/newsimage_form.html'
    success_message = "Запись успешно обновлено!"
       
    
class NewsImageDeleteView(LoginRequiredMixin, NewsGalleryView, DeleteView):
    template_name = 'admin/pages/news-gallery/newsgallery_confirm_delete.html'
    success_message = "Запись успешно удалено!"
    
def newsimage_delete(request, id):
    context = {}
    obj = get_object_or_404(PhotosNews, id = id)
    if request.method =="POST":
        try:
            if len(obj.URL) > 0:
                os.remove(obj.URL.path)
            obj.delete()
            
            messages.success(request, "Запись успешно удалено!")
            return redirect("newsimage_all")
        except Exception as e:
            messages.error(request, e)
            return redirect("newsimage_delete")
    return render(request, "admin/pages/news-image/newsimage_confirm_delete.html", context)
"""
---- End News-Image Views
"""    


"""
---- Project-Gallery Views
"""  
class ProjectGalleryView(View):
    model = GalleryProject
    form_class = ProjectGalleryForm
    success_url = reverse_lazy("projectgallery_all")
    extra_context = {
        "is_active" : "projects-panel",
        "active_project_gallery" : "active",
        "expand_projects" : "show",
        }
    
class ProjectGalleryListView(LoginRequiredMixin, ProjectGalleryView, ListView):
    login_url = "login_page"
    template_name = "admin/pages/project-gallery/gallery_list.html"

class ProjectGalleryCreateView(LoginRequiredMixin, SuccessMessageMixin, ProjectGalleryView, CreateView):
    login_url = "login_page"
    template_name = "admin/pages/project-gallery/gallery_create.html"
    redirect_field_name = "newsgallery_create"
    def get(self, request, *args, **kwargs):
        
        form = ProjectGalleryForm()
        context = {
            "form" : form,
            "is_active" : "gallery-panel",
            "expand_gallery" : "show",
            "active_create_gallerynews" : "active"
            
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ProjectGalleryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Запись Успешно добавлено!")
                return redirect(self.redirect_field_name)
            else:
                messages.error(request, "Введите валидные данные!")
                return redirect(self.redirect_field_name)
        else:
            messages.error(request, "Invalid Method")
            return redirect(self.redirect_field_name) 
        

class ProjectGalleryUpdateView(LoginRequiredMixin, SuccessMessageMixin, ProjectGalleryView, UpdateView):
    template_name = 'admin/pages/project-gallery/gallery_form.html'
    success_message = "Запись успешно обновлено!"      
    

def projectgallery_delete(request, id):
    context = {}
    obj = get_object_or_404(GalleryProject, id = id)
    if request.method =="POST":
        try:
        # delete object
            obj.delete()
        # after deleting redirect to
        # home page
            messages.success(request, "Запись успешно удалено!")
            return redirect("newsgallery_all")
        except RestrictedError:
            messages.error(request, "Вы не сможете удалить эту галерею, так как это связано с одной или несколькими проектами или фотографиями")
            return redirect("newsgallery_all")
    return render(request, "admin/pages/news-gallery/newsgallery_confirm_delete.html", context)
"""
---- End Project-Gallery Views
"""    



"""
---- Contest Views
"""  
class ContestView(View):
    model = Contests
    form_class = ContestForm
    success_url = reverse_lazy("contests_all")
    extra_context = {
        "is_active" : "contests-panel",
        "active_contests" : "active",
        "expand_contests" : "show",
        }
    

class ContestListView(LoginRequiredMixin, ContestView, ListView):
    login_url = "login_page"
    template_name = "admin/pages/contests/contests_list.html"
    

class ContestCreateView(LoginRequiredMixin, SuccessMessageMixin, ContestView, ListView):
    login_url = "login_page"
    template_name = "admin/pages/contests/contests_form.html"
    redirect_field_name = "contests_create"
    def get(self, request, *args, **kwargs):
        
        form = ContestForm()
        context = {
            "form" : form,
            "is_active" : "contests-panel",
            "expand_contests" : "show",
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContestForm(request.POST, request.FILES)
            try:
                form.save()
                messages.success(request, "Успешно добавлено!")
                return redirect(self.redirect_field_name)
            except ValueError:
                messages.error(request, "Выберите файлы в формате (.pdf, .docx, .doc)")
                return redirect(self.redirect_field_name)
            except Exception as e:
                messages.error(request, e)
                return redirect(self.redirect_field_name)
        else:
            messages.error(request, "Invalid Method")
            return redirect(self.redirect_field_name) 
        
class ContestUpdateView(LoginRequiredMixin, SuccessMessageMixin, ContestView, UpdateView):
    login_url = "login_page"
    template_name = "admin/pages/contests/contests_form.html"

def contests_delete(request, id):
    context = {}
    obj = get_object_or_404(Contests, id = id)
    if request.method =="POST":
        try:
            if len(obj.Document) > 0:
                os.remove(obj.Document.path)
            obj.delete()
            
            messages.success(request, "Запись успешно удалено!")
            return redirect("contests_all")
        except Exception as e:
            messages.error(request, e)
            return redirect("contests_delete")
    return render(request, "admin/pages/contests/contests_confirm_delete.html", context)



def get_last_projects(request):
    last_ten = Projects.objects.all().order_by('-id')[:10]
    template_name = "admin/admin.html"
    context = {
        "last_projects" : last_ten
    }
    
    return render(request, template_name, context)
>>>>>>> 69018b9ef27a8f551a156c7e22d9e6dc2aaccc86
