from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Organization)
admin.site.register(Slider)

class ImagemediaInline(admin.TabularInline):
    model = ImageMedia
    extra = 5

class ImageAlbumAdmin(admin.ModelAdmin):
    inlines = [ ImagemediaInline, ]


admin.site.register(ImageAlbum,ImageAlbumAdmin)