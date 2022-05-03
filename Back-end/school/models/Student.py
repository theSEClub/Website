from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Student(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_id = models.PositiveIntegerField(
        validators=[MinValueValidator(3500000), MaxValueValidator(5000000)],
        unique=True
    )
