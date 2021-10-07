from django.urls import path

from blog.models import blog
from .views import blogView

urlpatterns = [
    # path('blog/getAll',include('blog/urls.py')),
    path('',blogView.as_view()),
]