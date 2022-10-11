from django.contrib import admin
from .models import *

admin.site.register(Language)
admin.site.register(Projects)
admin.site.register(ProjectCategory)
admin.site.register(Contests)
admin.site.register(ContestsCategory)
admin.site.register(PhotosContests)
admin.site.register(GalleryNews)
admin.site.register(PhotosNews)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Language')