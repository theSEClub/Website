from django.contrib import admin
from .Models import SocialMedia

class SocialMediaAdmin(admin.ModelAdmin):
    list_display=['platform_name','link']
    list_editable=['link']
    search_fields=['platform_name']

admin.site.register(SocialMedia,SocialMediaAdmin)
