from django.contrib import admin
from main.models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
