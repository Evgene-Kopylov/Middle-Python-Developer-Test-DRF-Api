from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Books', views.BookViewSet, basename='Books')
router.register(r'Publishers', views.PublisherViewSet, basename='Publishers')
router.register(r'Authors', views.AuthorViewSet, basename='Authors')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

