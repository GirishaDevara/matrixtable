from django.urls import path
from . import views

urlpatterns = [
    # path('/<int:val1>/<int:val2>', views.add),
    path('<int:val1>/<int:val2>',views.table),
    path("showform",views.showform),
    path("showform/showdata",views.showdata),
    path("grade",views.grade),
    path("inheritance",views.inher),
    path("staticform",views.staticform),
    path("home",views.home),
    path("contacts",views.contacts),
    path("home2",views.homeinheritance),
    path("contactform",views.contactform, name = "contactf"),
    ]