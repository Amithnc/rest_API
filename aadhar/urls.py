from django.urls import path
from . import views
urlpatterns = [
    path('data/<str:number>',views.homepage),
    path('add-deatils/',views.add_detais),
    path('getstatus/',views.getstatus),
]