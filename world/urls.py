from django.urls import path
from . import views

app_name = "world"
urlpatterns = [
    path('', views.index, name="index"),
    path('country/<int:id>', views.country, name="country"),
]