from django.contrib import admin
from .models import Primary, Secondary, PrimaryAlbum, SecondaryAlbum

admin.site.register(Primary)
admin.site.register(Secondary)
admin.site.register(PrimaryAlbum)
admin.site.register(SecondaryAlbum)

