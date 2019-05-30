from django.contrib import admin
from .models import Subject,Author,Preprint,Tag

# Register your models here.

admin.site.register(Subject)
admin.site.register(Author)
admin.site.register(Preprint)
admin.site.register(Tag)