from main.models import Image, Group
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group as Gr

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'group')
    list_filter = ('group', 'pub_date')

admin.site.register(Image, ImageAdmin)
admin.site.register(Gr)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)