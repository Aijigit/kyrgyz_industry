from django.shortcuts import render

# Create your views here.


def index(request):
    template_name = "index.html"
    return render(request, template_name, {})


def detail(request):
    template_name = "blog_detail.html"
    return render(request, template_name, {})