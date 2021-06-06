from django.urls import path 
from . import views

urlpatterns = [
    #If at base url, it shows views.index as the HTML.
    path("", views.v1, name="view 1"),
    path("<int:id>", views.index, name="index")
]