from django.contrib import admin
from users.models import UserProfile
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserProfileAdmin(UserAdmin):
    list_display = ("username","password","nick_name")
admin.site.register(UserProfile,UserProfileAdmin)