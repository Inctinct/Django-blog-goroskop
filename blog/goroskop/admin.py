from django.contrib import admin
from .models import Goroskop
# Register your models here.


class GoroskopAdmin(admin.ModelAdmin):
    list_display = ('title','text','date')
    list_filter = ('title',)


admin.site.register(Goroskop, GoroskopAdmin)