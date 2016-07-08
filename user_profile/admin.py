from django.contrib import admin
from user_profile.models import UserProfile, University, Career, Subject, Area, ReunionSite
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ['user']


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']


class ReunionAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']


class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']

# Register user_profile models in the admin.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(ReunionSite, ReunionAdmin)
