from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from hours.models import Projects
from projects.models import Project

#admin.site.register(User, UserAdmin)

@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets
