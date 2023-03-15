from django.contrib import admin
from .models import Primary, PrimaryResult, ScienceAlbums, Art, ArtAlbums, AlbumA, AlbumC, AlbumS, Commerce, CommerceAlbums, Science

# Register your models here.
admin.site.register(Primary)
admin.site.register(PrimaryResult)
admin.site.register(ScienceAlbums)
admin.site.register(Art)
admin.site.register(ArtAlbums)
admin.site.register(Commerce)
admin.site.register(CommerceAlbums)
admin.site.register(Science)
admin.site.register(AlbumS)
admin.site.register(AlbumC)