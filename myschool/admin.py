from django.contrib import admin
from .models import Primary, Secondary, PrimaryAlbum, SecondaryAlbum, SchoolBoard, Contact,ResultClass, SectionPrimary

admin.site.register(ResultClass)
admin.site.register(SectionPrimary)
admin.site.register(Primary)
admin.site.register(Secondary)
admin.site.register(PrimaryAlbum)
admin.site.register(SecondaryAlbum)
admin.site.register(SchoolBoard)
admin.site.register(Contact)

