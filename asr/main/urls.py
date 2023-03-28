from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('about/', about_us, name='about'),
    path('portfolio/', porfolio, name='portfolio'),
    path('portfolio_detail/<slug:post>/', portfolio_detail, name='portfolio_detail'),
    path('news/', news, name='news'),
    path('news_detail/<slug:post>/', news_detail, name='news_detail'),
    path('rubrics/<int:id>/', filtered_news, name='filter'),
    path('archive/<int:year>/',
         ArticleYearArchiveView.as_view(),
         name="article_year_archive"),
    path('contact/', contact, name='contact'),
]
