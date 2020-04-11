from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    # path("contacts",views.contacts, name= 'contacts'),
    # path("about",views.about, name= 'about'),
    path("edit/<int:id>",views.edititem, name= 'edit'),
    path("create",views.create),
    path("delete/<int:id>",views.delete, name = 'delete'),
    path("<int:id>",views.itemdetails, name = 'itemdetails')
    ]