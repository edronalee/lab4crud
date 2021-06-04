from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addauthor/', views.addauthor, name="addauthor"),
    path('addbook/', views.addbook, name="addbook"),
    path('deleteauthor/<str:pk>', views.deleteauthor, name="deleteauthor"),
    path('deletebook/<str:pk>', views.deletebook, name="deletebook"),
    path('updateauthor/<str:pk>', views.updateauthor, name="updateauthor"),
    path('updatebook/<str:pk>', views.updatebook, name="updatebook"),
]
