from rest_framework import serializers
from authenticator.serializers import UserRetrieveSerializer

from school.models import Student


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'user']


class StudentRetrieveSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()

    class Meta:
        model = Student
        fields = ['student_id', 'user']
