from enum import unique
from tabnanny import verbose
from tokenize import Name
from django.db import models

# Языки
class Language(models.Model):
    Name=models.CharField(max_length=10,verbose_name="Язык")

    class Meta:
        db_table="language" 

# Категория проектов
class ProjectCategory(models.Model):
    Name=models.CharField(max_length=70,verbose_name="Название категории")
    
    class Meta:
        db_table="projectCategory" 

# Категория конкурсов
class ContestsCategory(models.Model):
    Name=models.CharField(max_length=70,verbose_name="Название категории")
    
    class Meta:
        db_table="contestsCategory"   

#Галерея 
class GalleryProject(models.Model):
    Name=models.CharField(max_length=50,verbose_name="Название галереи")

    class Meta:
        db_table="galleryProject" 


class GalleryContests(models.Model):
    Name=models.CharField(max_length=50,verbose_name="Название галереи")

    class Meta:
        db_table="galleryContests"


class GalleryNews(models.Model):
    Name=models.CharField(max_length=50,verbose_name="Название галереи")

    class Meta:
        db_table="galleryNews" 

# Фото 
class PhotosProject(models.Model):
    URL=models.FilePathField(verbose_name="Путь картинки")
    Title=models.CharField(max_length=70,verbose_name="Заголовок картинки")
    Gallery=models.ForeignKey("galleryProject",on_delete=models.CASCADE,verbose_name="Галерея")


class PhotosContests(models.Model):
    URL=models.FilePathField(verbose_name="Путь картинки")
    Title=models.CharField(max_length=70,verbose_name="Заголовок картинки")
    Gallery=models.ForeignKey("galleryProject",on_delete=models.CASCADE,verbose_name="Галерея")


class PhotosNews(models.Model):
    URL=models.FilePathField(verbose_name="Путь картинки")
    Title=models.CharField(max_length=70,verbose_name="Заголовок картинки")
    Gallery=models.ForeignKey("galleryProject",on_delete=models.CASCADE,verbose_name="Галерея")


# Проекты

class Projects(models.Model):
    Title=models.CharField(max_length=70,verbose_name="Заголовок проекта")
    Discription=models.TextField(verbose_name="Описание")
    Date_added=models.DateField(verbose_name="Дата публикации")
    Language=models.ForeignKey("language",on_delete=models.CASCADE,verbose_name="Язык")
    Gallery=models.ForeignKey("galleryProject",on_delete=models.CASCADE,verbose_name="Галерея")
    Category=models.ForeignKey("projectCategory",on_delete=models.CASCADE,verbose_name="Категория")


# Конкурсы

class Contests(models.Model):
    Title=models.CharField(max_length=70,verbose_name="Заголовок конкурса")
    Discription=models.TextField(verbose_name="Описание")
    Date_added=models.DateField(verbose_name="Дата публикации")
    Language=models.ForeignKey("language",on_delete=models.CASCADE,verbose_name="Язык")
    Gallery=models.ForeignKey("galleryContests",on_delete=models.CASCADE,verbose_name="Галерея")
    Category=models.ForeignKey("contestsCategory",on_delete=models.CASCADE,verbose_name="Категория")

# Новости

class News(models.Model):
    Title=models.CharField(max_length=70,verbose_name="Заголовок новости")
    Discription=models.TextField(verbose_name="Описание")
    Date_added=models.DateField(verbose_name="Дата публикации")
    Language=models.ForeignKey("language",on_delete=models.CASCADE,verbose_name="Язык")
    Gallery=models.ForeignKey("galleryNews",on_delete=models.CASCADE,verbose_name="Галерея")

