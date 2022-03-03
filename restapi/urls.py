from django.urls import path, include
from .views import article_list_view, article_detail_view, ArticleAPIView, ArticleDetailView, GenericAPIView, ArticleViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
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
