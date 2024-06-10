from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from bichan.records.api.serializers import RecordSerializer, RoleSerializer, UserSerializer
from bichan.records.models import Record

class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    @action(methods=['get'], detail=False)
    def ceo(self, request, format = None):
        data = Group.objects.filter(name="CEO").first().records.all()
        labels = [item.name for item in data]
        values = [item.value for item in data]

        res = {
            "labels": labels,
            "values": values,
            "name": "CEO",
        }

        return Response(res)

    @action(methods=['get'], detail=False)
    def econ(self, request, format = None):
        data = Group.objects.filter(name="ECON").first().records.all()
        labels = [item.name for item in data]
        values = [item.value for item in data]

        res = {
            "labels": labels,
            "values": values,
            "name": "ECON",
        }

        return Response(res)

class RoleViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
