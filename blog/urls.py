from django.urls import path

from blog.models import blog
from .views import blogView, blog_filterbytitle_view, blog_returnFirstTen_view, blog_incViews_view, blog_getMostViewedblog, blog_filterbyTag_view

urlpatterns = [
    # path('blog/getAll',include('blog/urls.py')),
    path('getall',blogView.as_view()),
    path('getall/filter',blog_filterbytitle_view.as_view()),
    path('getall/getfirstten',blog_returnFirstTen_view.as_view()),
    path('getall/incview',blog_incViews_view.as_view()),
    path('getall/mostviewed',blog_getMostViewedblog.as_view()),
    path('getall/bytag',blog_filterbyTag_view.as_view()),
]