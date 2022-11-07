from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.core.mail import BadHeaderError, send_mail
from django.core import mail
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
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
    template_name = "admin/pages/forms/login.html"
    
    return render(request, template_name, {})

@csrf_exempt
def authorization(request):
    success_url = reverse_lazy('admin_panel')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(success_url)
    else:
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
    fields = '__all__'
    success_url = reverse_lazy('news_all')
    extra_context = {
        "is_active" : "news-panel",
        "expand" : "show"
        }

class NewsListView(LoginRequiredMixin, NewsView, ListView):
    login_url = 'login_page'
    template_name = 'admin/pages/news/news-all.html'
    

def ProjectsGetAll(request):
    projects = Projects.objects.all()
    return render(request, 'client/index.html', {'project':projects})