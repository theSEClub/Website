from rest_framework.viewsets import ModelViewSet

from school.models import Student
from school.serializers import StudentRetrieveSerializer, StudentCreateSerializer


class StudentViewSet(ModelViewSet):
    serializer_class = StudentRetrieveSerializer
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StudentCreateSerializer
        elif self.request.method == 'GET':
            return StudentRetrieveSerializer
