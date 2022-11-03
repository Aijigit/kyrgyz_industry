from email.policy import default
from enum import unique
from random import choices
from tabnanny import verbose
from tokenize import Name
from xmlrpc.client import DateTime
from django.db import models
from django.utils.timezone import now

# Языки
class LanguageChoice(models.TextChoices):
    RU = "Русский", "Русский"
    KG = "Кыргызча", "Кыргызча"
    EN = "English", "English"
    CH = "中国人", "中国人"
    
  
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
    def __str__(self) -> str:
        return self.Name   
# Фото 
class PhotosProject(models.Model):
    URL=models.FileField(verbose_name="Путь к картинке")
    Caption=models.CharField(max_length=70,verbose_name="Название картинки", default='')
    Gallery=models.ForeignKey("galleryProject",on_delete=models.RESTRICT,verbose_name="Галерея")


class PhotosContests(models.Model):
    URL=models.FileField(verbose_name="Путь картинки")
    Caption=models.CharField(max_length=70,verbose_name="Название картинки", default='')
    Gallery=models.ForeignKey("galleryProject",on_delete=models.RESTRICT,verbose_name="Галерея")


class PhotosNews(models.Model):
    URL=models.FileField(verbose_name="Путь картинки")
    Caption=models.CharField(max_length=70,verbose_name="Название картинки", default='')
    Gallery=models.ForeignKey("galleryProject",on_delete=models.RESTRICT,verbose_name="Галерея")

class Contest_Status_Choice(models.TextChoices):
    ON_PROCCESS = "В процессе", "В процессе"
    HAS_FINISHED = "Проведён", "Проведён"
    NOT_FINISHED = "Не Проведён", "Не Проведён"
class Project_Status_Choice(models.TextChoices):
    ON_PROCCESS = "В процессе", "В процессе"
    HAS_FINISHED = "Реализован", "Реализован"
    NOT_FINISHED = "Не реализован", "Не реализован"

# Проекты
class Projects(models.Model):
    Title=models.CharField(max_length=70,verbose_name="Заголовок проекта")
    Description=models.TextField(verbose_name="Описание")
    Date_added=models.DateTimeField(verbose_name="Дата публикации", default=now)
    # Язык проекта
    Language=models.CharField(
                               max_length = 10, 
                               choices = LanguageChoice.choices,
                               default = LanguageChoice.RU,
                               verbose_name = "Язык"
                             )
    Gallery=models.ForeignKey(
        "galleryProject",
        on_delete=models.RESTRICT,
        verbose_name="Галерея"
        )
    Category=models.ForeignKey(
        "projectCategory",
        on_delete=models.RESTRICT,
        verbose_name="Категория"
        )
    Status = models.CharField(
        max_length = 20,
        choices = Project_Status_Choice.choices,
        default = Project_Status_Choice.ON_PROCCESS,
        verbose_name = "Статус"
    )

# Конкурсы

class Contests(models.Model):
    Title=models.CharField(max_length=70,verbose_name="Заголовок конкурса")
    Short_Description = models.CharField(max_length=110,verbose_name="Краткое описание", default ='')
    Description=models.TextField(verbose_name="Описание")
    Document = models.FileField(verbose_name="Документ")
    Date_added=models.DateTimeField(verbose_name="Дата публикации", default=now)
    Language=models.CharField(
                               max_length = 10, 
                               choices = LanguageChoice.choices,
                               default = LanguageChoice.RU,
                               verbose_name = "Язык"
                               )
    Gallery=models.ForeignKey("galleryContests",on_delete=models.RESTRICT,verbose_name="Выберите Галерую")
    Category=models.ForeignKey("contestsCategory",on_delete=models.RESTRICT,verbose_name="Выберите Категорию")
    Status = models.CharField(
        max_length = 20,
        choices = Contest_Status_Choice.choices,
        default = Contest_Status_Choice.ON_PROCCESS,
        verbose_name = "Статус"
    )

# Новости

class News(models.Model):
    Title=models.CharField(max_length=70,verbose_name="Заголовок новости")
    Short_Description = models.CharField(max_length=110,verbose_name="Краткое описание")
    Description=models.TextField(verbose_name="Описание")
    Date_added=models.DateTimeField(verbose_name="Дата публикации", default=now)
    Language= models.CharField(
                               max_length = 10, 
                               choices = LanguageChoice.choices,
                               default = LanguageChoice.RU,
                               verbose_name = "Язык"
                               )
    Gallery=models.ForeignKey("galleryNews",on_delete=models.RESTRICT,verbose_name="Галерея")

