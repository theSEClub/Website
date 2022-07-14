############################### Models File ####################################

from django.db import models

social_media_platforms=(
    ('Facebook','Facebook'),
    ('Instagram','Instagram'),
    ('Linkedin','Linkedin'),
    ('Snapchat','Snapchat'),
    ('Twitter','Twitter'),
)

class SocialMedia(models.Model):
    platform_name=models.CharField(max_length=255, choices=social_media_platforms)
    link=models.URLField()
    def __str__ (self):
        return self.platform_name
    class Meta:
        verbose_name='Social Media Link'
        ordering=['platform_name']


############################### serilaizer File ################################

from rest_framework import serializers 

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model= SocialMedia
        fields=['id','platform_name','link']

############################### views File #####################################

from rest_framework.viewsets import ModelViewSet

class SocialMediaViewSet(ModelViewSet):
    serializer_class=SocialMediaSerializer
    queryset=SocialMedia.objects.all()
    http_method_name=['get','post','patch','delete']