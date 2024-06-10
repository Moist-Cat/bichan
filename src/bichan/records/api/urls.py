from django.urls import path, include
from rest_framework import routers
from bichan.records.api import views

app_name = "records"

router = routers.DefaultRouter()
router.register("user", views.UserViewSet, basename="User")
router.register("role", views.RoleViewSet, basename="Role")
router.register("record", views.RecordViewSet, basename="Records")

urlpatterns = [
    path("", include(router.urls)),
    path("record/", views.RecordViewSet.as_view({"get": "ceo"}),),
    path("record/", views.RecordViewSet.as_view({"get": "econ"}),),
]
