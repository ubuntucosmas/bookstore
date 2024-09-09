from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary_view, name='view_basket'),
    path('add/', views.add_to_basket, name='add_to_basket'),

]