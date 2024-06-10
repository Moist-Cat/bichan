from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User, Group

from rest_framework import serializers

from bichan.records.models import Record

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class RecordSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True, many=False)
    class Meta:
        model = Record
        fields = [
            "id",
            "name",
            "value",
            "role",
        ]
