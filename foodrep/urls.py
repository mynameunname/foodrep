from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.food_list, name='food_list'),
]
