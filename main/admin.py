from main.models import Image, Group
from django.contrib import admin

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'group')
    list_filter = ('group', 'pub_date')

admin.site.register(Image, ImageAdmin)
admin.site.register(Group)
