####################### Models File #########################
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from django.db import models


class IntershipInfo(models.Model):
    position = models.CharField(max_length=200)
    entity_name = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True)
    advertisement = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Intership Information'


class COOPInfo(models.Model):
    position = models.CharField(max_length=200)
    entity_name = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True)
    advertisement = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'COOP Information'


class MinorsInfo(models.Model):
    Minors = (
        ('Artifical Intelligence (AI)', 'Artifical Intelligence (AI)'),
        ('Cyber Security (FC)', 'Cyber Security (FC)'),
    )
    minor_in = models.CharField(max_length=50, choices=Minors)
    plan = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)

    def __str__(self):
        return self.minor_in

    class Meta:
        verbose_name = 'Minors Information'
##########################################################################################


################################ Serilizer File ##########################################


class IntershipInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntershipInfo
        fields = ['position', 'entity_name', 'link', 'advertisement']


class COOPInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = COOPInfo
        fields = ['position', 'entity_name', 'link', 'advertisement']


class MinorsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinorsInfo
        fields = ['minor_in', 'plan']
###############################################################################


##################################### View File ################################


class IntershipInfoViewSet(ModelViewSet):
    serializer_class = IntershipInfoSerializer
    queryset = IntershipInfo.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']


class COOPInfoViewSet(ModelViewSet):
    serializer_class = COOPInfoSerializer
    queryset = COOPInfo.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']


class MinorsInfoViewSet(ModelViewSet):
    serializer_class = MinorsInfoSerializer
    queryset = MinorsInfo.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
