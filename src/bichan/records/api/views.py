from rest_framework.viewsets import ModelViewSet
from bichan.records.api.serializers import RecordSerializer

from bichan.records.models import Record

class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
