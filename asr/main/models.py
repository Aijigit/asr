from django.db import models
from ckeditor.fields import RichTextField 
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from PIL import Image
import uuid
import os

# Функция для кодировки название файла
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename_start = filename.replace(filename,'_f')
    filename = "%s__%s.%s" % (uuid.uuid4(),filename_start, ext)
    return os.path.join(instance.path_url, filename)
        
class Projects(models.Model):
    class Sizes(models.TextChoices):
        W1 = 'gridy-1', _('Ширина 25%')
        W2 = 'gridy-2', _('Ширина 50%')
        W3 = 'gridy-3', _('Ширина 75%')
        H1 = 'gridyhe-1', _('Высота 25%')
        H2 = 'gridyhe-2', _('Высота 50%')
    class Status(models.TextChoices):
        DONE = 'Реализован', _('Реализован')
        PROC = 'В Процессе', _('В Процессе')    
        
    class Categories(models.TextChoices):
        ARCH = 'architecture', _('Архитектура')
        DES = 'design', _('Дизайн')
        CONS = 'construction', _('Строительство')
    # Обложка
    img_thumb = models.ImageField(verbose_name='Обложка для главного' , upload_to=get_file_path)
    img_bg = models.ImageField(verbose_name='Обложка для бокового(Вертикально)' , upload_to=get_file_path, default='')
    width = models.CharField(max_length=10, verbose_name='Ширина Изображении для Грид сетки', choices=Sizes.choices, default = Sizes.W1, help_text='Откройте страницу Портфолио, и сразу посмотрите на расположение фотографии. Это важно!')
    height = models.CharField(max_length=10, verbose_name='Высота Изображении для Грид сетки', choices=Sizes.choices, default = Sizes.H1,
                              help_text='Откройте страницу Портфолио, и сразу посмотрите на расположение фотографии. Это важно!')
    category  = models.CharField(verbose_name='Категория', max_length=20, choices=Categories.choices, default=Categories.ARCH)
    title = models.CharField(verbose_name='Название проекта', max_length=150)
    short_description = models.CharField(verbose_name='Краткое описание проекта', max_length=250, help_text='250 символов') 
    description = RichTextField(verbose_name='Полное описание проекта')
    address = models.CharField(max_length=200, verbose_name='Адрес', null=True)
    square = models.IntegerField(verbose_name='Площадь(КВ, М)', null=True)
    status = models.CharField(max_length=20, verbose_name='Статус', choices=Status.choices, default=Status.PROC, null=True)
    author = models.CharField(max_length=200, verbose_name='Авторский коллектив', null=True)
    date_added = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
    slug = models.SlugField(default='', null=False)
    
    path_url = "static/main/img/projects/"
    
    def __str__(self):
        return f"{self.title} {self.short_description}"
    
    def get_absolute_url(self):
        return self.reverse('portfolio_detail', kwargs = {"slug" : self.slug})
    
    class Meta:
        verbose_name = 'Портфолио'


class ProjectImage(models.Model):
    url = models.ImageField(upload_to=get_file_path, verbose_name='Выберите фотографию')
    project = models.ForeignKey(Projects, on_delete=models.RESTRICT, related_name = 'project_img')    
    
    path_url = "static/main/img/projects/"
    
    def save(self, *args, **kwargs):
       super(ProjectImage, self).save(*args, **kwargs)
       image = Image.open(self.url.path)
       image.save(self.url.path,quality=20,optimize=True)
      
    def __str__(self):
        return self.project.title
    
    class Meta:
        verbose_name = 'Фотографии для Портфолио'     

        
        
class NewsCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория Новости'
        

        
        
class News(models.Model):
    thumb = models.ImageField(upload_to=get_file_path)
    title = models.CharField(max_length=150, verbose_name='Название новости')
    short_description = models.TextField(max_length=500 ,verbose_name='Краткое описание')
    description = RichTextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.RESTRICT, verbose_name='Категория')
    date_added = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    
    slug = models.SlugField(null = False, unique = True)
    
    path_url = "static/main/img/news/"
    
    def __str__(self):
        return f"{self.title} {self.category}"
    
    
    def get_absolute_url(self):
        return self.reverse("news_detail", kwargs = {"slug" : self.slug})
    
    class Meta:
        verbose_name = 'Новости'
        
class NewsImage(models.Model):
    url = models.ImageField(upload_to=get_file_path)  
    news = models.ForeignKey(News, on_delete=models.RESTRICT)
    
    
    path_url = "static/main/img/news/"
    
    def __str__(self):
        return self.news.title
    
    class Meta:
        verbose_name = 'Изображения для Новости'

     
class Awards(models.Model):
    picture = models.ImageField(upload_to=get_file_path)
    title = models.CharField(max_length=130, verbose_name='Название награды')
    description = models.CharField(max_length=255, verbose_name='Краткое описание')
    slug = models.SlugField(max_length=130, unique=True)
    
    path_url = "static/main/img/awards/"
    
    def save(self, *args, **kwargs):
       super(Awards, self).save(*args, **kwargs)
       image = Image.open(self.picture.path)
       image.save(self.picture.path,quality=5,optimize=True)
      
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Награды'
        
class Partners(models.Model):
    img = models.ImageField(upload_to=get_file_path, verbose_name='Логотип')
    name = models.CharField(max_length=250, verbose_name='Название компании')
    
    path_url = "static/main/img/partners/"
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name='Партнеры'
        


class Team(models.Model):
    img = models.ImageField(verbose_name='Фотография', upload_to=get_file_path)
    full_name = models.CharField(verbose_name='ФИО Сотрудника', max_length=150)
    position = models.CharField(verbose_name='Должность', max_length=50)
    instagram = models.CharField(verbose_name='Ссылка на Инста профиль', max_length=250, null=True)
    facebook = models.CharField(verbose_name='Ссылка на FaceBook', max_length=250, null=True)
    telegram = models.CharField(verbose_name='Ссылка на Телеграм', max_length=250, null=True)
    
    path_url = "static/main/img/team/"
    
    def __str__(self):
        return self.full_name 
    class Meta:
        verbose_name='Наша команда'