from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Publisher', views.PublisherViewSet, basename='Publisher')
router.register(r'Author', views.AuthorViewSet, basename='Author')
router.register(r'Book', views.BookViewSet, basename='Book')


urlpatterns = [
    path('', include(router.urls)),
    path('books_info/<int:page>/<int:size>/', views.books_info),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
