from django.urls import path
from .views import main_page, catalog_page

urlpatterns = [
    path("", main_page),
    path("catalog/", catalog_page)
]
