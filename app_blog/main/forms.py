from dataclasses import fields
from typing import Text
from .models import *
from django.forms import ModelForm, DateTimeInput, TextInput, Textarea
from django import forms
from django.utils.translation import gettext_lazy as _


# News
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['Title', 'Short_Description', 'Description', 'Date_added', 'Language', 'Gallery']
    
        widgets = {
            'Title' : TextInput(
                attrs = {"type" : "text", "class" : "form-control", "id" : "title", "placeholder" : "Название новости","size" : 70, 'required': True}
            ),
            'Short_Description' : TextInput(
                attrs = {"type" : "text", "class" : "form-control", "id" : "short_description", "placeholder" : "Краткое описание", "size" : 110, 'required': True}
            ),
            'Description' : Textarea(
                attrs = {"class" : "form-control", "id" : "description", "placeholder" : "Полное содержание", 'required': True}
                ),
            'Date_added' : DateTimeInput(
                attrs={'type': 'datetime-local', "class" : "form-control", "id" : "date_created", "required" : False}
                ),
            'Language' : forms.Select(
                attrs={"class": "form-control", 'required': True,  "id" : "language"},
                choices=LanguageChoice.choices
            ),
            'Gallery' : forms.Select(
                attrs={"class": "form-control", 'required': True, "id" : "gallery"}
            )
        }
        
    def check_for_empty(self):
        title = self.cleaned_data.get("Title")
        short_description = self.cleaned_data.get("Short_Description")
        description = self.cleaned_data.get("Description")
        gallery = self.cleaned_data.get("Gallery")
        if title == "" or short_description == "" or description == "" or gallery == "":
            raise forms.ValidationError('Это поле обязательное!')
        return title   
   
# Форма для Галереи
class NewsGalleryForm(ModelForm):
    class Meta:
        model = GalleryNews
        fields = ["Name"]
        widgets = {
            'Name' : TextInput(
                attrs= {"type" : "text", "class" : "form-control", "id" : "name", "placeholder" : "Название  галереи", "required" : True })
        } 
        
# Форма для изображение новости
class NewsImageForm(ModelForm):
    class Meta:
        model = PhotosNews
        fields = ["URL", "Caption", "Gallery"]
        
        widgets = {
            'URL' : forms.FileField(),
            'Caption' : TextInput(
                attrs = {"type" : "text", "class" : "form-control", "id" : "image-caption", "placeholder" : "Описание изображении", "size" : 110, 'required': False}
            ),
            'Gallery' : forms.Select(
                attrs={"class": "form-control", 'required': True, "id" : "gallery"}
            )
        }
        
# Projects    
class ProjectImageFrom(ModelForm):
    class Meta:
        model = PhotosProject
        fields = ["URL", "Caption", "Gallery"]
        
        widgets = {
            'URL' : forms.FileField(),
            'Caption' : TextInput(
                attrs = {"type" : "text", "class" : "form-control", "id" : "image-caption", "placeholder" : "Описание изображении", "size" : 110, 'required': False}
            ),
            'Gallery' : forms.Select(
                attrs={"class": "form-control", 'required': True, "id" : "gallery"}
            )
        }
        
# Project Form
class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['Title',  'Description', 'Date_added', 'Language', 'Gallery', 'Category', 'Status']
        widgets = {
            'Title' : TextInput(
                attrs = {"type" : "text", "class" : "form-control", "id" : "title", "placeholder" : "Название новости","size" : 70, 'required': True}
            ),
            'Description' : Textarea(
                attrs = {"class" : "form-control", "id" : "description", "placeholder" : "Полное содержание", 'required': True}
                ),
            'Date_added' : DateTimeInput(
                attrs={'type': 'datetime-local', "class" : "form-control", "id" : "date_created", "required" : False}
                ),
            'Language' : forms.Select(
                attrs={"class": "form-control", 'required': True,  "id" : "language"},
                choices=LanguageChoice.choices
            ),
            'Gallery' : forms.Select(
                attrs={"class": "form-control", 'required': True, "id" : "gallery"}
            ),
            'Category' : forms.Select(), 
            'Status' : forms.Select()
        }