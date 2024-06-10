from django.urls import path, include
from django.contrib.auth.decorators import login_required

from bichan.records import views
from bichan.records.api import urls as api_urls

urlpatterns = [
    path("", include(api_urls)),
    path("view", login_required(views.HomeView.as_view()))
    #path("create/", views.create, name = "create_record"),
    #path("retrieve/<id>/", views.retrieve, name="retrieve_record"),
    #path("update/<id>/", views.update, name="update_record"),
    #path("delete/<id>/", views.delete, name="delete_record"),
]
