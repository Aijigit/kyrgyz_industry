from django.shortcuts import render

# Create your views here.


def index(request):
    template_name = "client/index.html"
    return render(request, template_name, {})


def detail(request):
    template_name = "client/pages/blog_detail.html"
    return render(request, template_name, {})

def admin_index_page(request):
    template_name = "admin/admin.html"
    return render(request, template_name, {})

def admin_form_page(request):
    template_name = "admin/pages/forms/basic_elements.html"
    return render(request, template_name, {})