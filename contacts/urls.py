from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('<int:id>/', views.delete, name='delete'),

]
