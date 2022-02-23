from re import A
from django.urls import path
from .views import article_list_view, article_detail_view, ArticleAPIView, ArticleDetailView, GenericAPIView

urlpatterns = [
    # ================function based =================================

    # path('article/', article_list_view),
    # path('article/<int:pk>/', article_detail_view),

    # ============================class based=========================

    path('article/<int:pk>/', ArticleDetailView.as_view()),
    path('article/', ArticleAPIView.as_view()),

    # ====================generic views|mixins==============================

    path('article/generic/<int:id>/', GenericAPIView.as_view()),
    path('article/generic/', GenericAPIView.as_view()),

]
