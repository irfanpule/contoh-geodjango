from django.urls import path
from . import views

app_name = "indonesia"
urlpatterns = [
    path('', views.index, name="index"),
    path('provinsi/<int:id>', views.provinsi, name="provinsi"),
]