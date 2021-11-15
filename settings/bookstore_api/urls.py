from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'publisher', views.PublisherViewSet, basename='publisher')
router.register(r'edit_publisher', views.Edit_PublisherViewSet, basename='edit_publisher')
router.register(r'author', views.AuthorViewSet, basename='author')
router.register(r'edit_author', views.Edit_AuthorViewSet, basename='edit_author')
router.register(r'book', views.BookViewSet, basename='book')
router.register(r'edit_book', views.Edit_BookViewSet, basename='edit_book')


schema_view = get_schema_view(
   openapi.Info(
      title="Bookstore API",
      default_version='v1',
      description="Api doc for MYFI Middle Python Developer Test. \
                    Complited by Kopylov Evgene. t.me @EvgeneKopylov",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="eugenevkopylov@gmail.com"),
      license=openapi.License(name="GNU_v3"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('items/', include(router.urls)),
    path('publishers_info/<int:page>/<int:size>/', views.publishers_info),
    path('authors_info/<int:page>/<int:size>/', views.authors_info),
    path('books_info/<int:page>/<int:size>/', views.books_info),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),

    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

]
