from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name=None),
]
