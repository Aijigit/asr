from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from next_prev import next_in_order, prev_in_order
from django.views.generic.dates import YearArchiveView

"""
    1. Главная +
    2. О нас
    3. Портфолио +
        3.1. Детальная страница +
    4. Награды
    5. Контакты +
    6. Новости
        6.1. Детальная страница
"""

is_active = "link-active"

def index(request):
    pr_count = Projects.objects.all().count()
    aw_count = Awards.objects.all().count()
    parnters_count = Partners.objects.all().count()
    
    projects = Projects.objects.all().order_by('-id')[:10]
    awards = Awards.objects.all().order_by('-id')[:10]
    partners = Partners.objects.all().order_by('-id')[:10]
    context = {
        "home_active" : is_active,
        "projects" : projects,
        "awards" : awards,
        "partners" : partners,
        "pr_count" : pr_count,
        "aw_count" : aw_count,
        "pn_count" : parnters_count
    }
    return render(request, 'main/index.html', context)


def about_us(request):
    page_title = "О компании"
    aw_count = Awards.objects.all().count()
    
    team = Team.objects.all()
    awards = Awards.objects.all().order_by('-id')
    context = {
        "page_title" : page_title,
        "about_active" : is_active,
        "teams" : team,
        "awards" : awards
    }
    return render(request, 'main/about.html', context)


class ArticleYearArchiveView(YearArchiveView):
    template_name = "main/archive-year.html"
    queryset = News.objects.all()
    date_field = "date_added"
    make_object_list = True
    allow_future = True
    
    

def porfolio(request):
    page_title = "Портфолио"
    
    projects = Projects.objects.all()
    
    context = {
        "page_title" : page_title,
        "projects" : projects,
        "portfolio_active" : is_active
    }
    return render(request, 'portfolio.html', context)


def portfolio_detail(request, post):
    page_title = "Детальная страница"
    
    post = get_object_or_404(Projects, slug=post)   
    images = ProjectImage.objects.filter(project_id = post.id) 
    count = ProjectImage.objects.filter(project_id = post.id).count()
    context = {
        "page_title" : page_title,
        "post" : post,
        "images" : images,
        "count" : count,
      
    }

    return render(request, 'portfolio-detail.html', context)


def news(request):
    page_title = "Новости"
    
    news = News.objects.all().order_by('-date_added')
    awards = Awards.objects.all().order_by('-id')
    
    context = {
        "page_title" : page_title,
        "news" : news,
        "news_active" : is_active,
        "awards" : awards
    }

    return render(request, 'main/news.html', context)

def filtered_news(request, id):
    news = News.objects.filter(category_id=id).order_by('-date_added')
    category = get_object_or_404(NewsCategory, id=id)
    page_title = category.name
    
    context = {
        "page_title" : page_title,
        "news" : news,
        "news_active" : is_active
    }

    return render(request, 'main/news.html', context)

def news_detail(request, post):
    page_title = "Новости"
    posts = News.objects.all()
    post = get_object_or_404(News, slug=post)
    last_five = News.objects.all().order_by('-date_added')[:5]
    rubrics = NewsCategory.objects.all()
    images = NewsImage.objects.filter(news_id = post.id) 
    
    first_object = News.objects.first()
    last_object = News.objects.last()
    next_object = next_in_order(post)
    check_next = next_object == last_object
    
    check_nxt = False
    if check_next:
        next_object = News.objects.last()
        check_nxt = True
        
   
    check_pr = False
    prev_object = prev_in_order(post, loop=True)
    check_prev = prev_object == first_object # True
    if check_prev:
        prev_object = first_object
        check_pr = True
  
    context = {
        "page_title" : page_title,
        "post" : post,
        "images" : images,
        "news_active" : is_active,
        "last_five" : last_five,
        "rubrics" : rubrics,
        "next" : next_object,
        "prev" : prev_object,
        "check_prev" : check_pr,
        "check_next" : check_nxt,
    }

    return render(request, 'main/news-detail.html', context)

def contact(request):
    page_title = "Контакты"
    
    context = {
        "page_title" : page_title,
        "contact_active" : is_active
    }

    return render(request, 'main/contact.html', context)

