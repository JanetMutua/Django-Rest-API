from re import A
from django.urls import path
from .views import article_list_view, article_detail_view

urlpatterns = [
    path('article/', article_list_view),
    path('article/<int:pk>/', article_detail_view)

]
