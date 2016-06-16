from django.contrib import admin
from user_profile.models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ['user']

admin.site.register(UserProfile, UserProfileAdmin)
