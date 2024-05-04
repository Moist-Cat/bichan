from django.urls import path, include
from rest_framework import routers
from bichan.records.api import views

app_name = "records"

router = routers.DefaultRouter()
router.register("record", views.RecordViewSet, basename="Records")

urlpatterns = [
    path("", include(router.urls)),
]
