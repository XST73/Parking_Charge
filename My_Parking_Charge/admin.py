from django.contrib import admin, messages

from .models import *


# Register your models here.

@admin.register(VIPuserInfo)
class UserInfo1(admin.ModelAdmin):
    list_display = ('user_nanme', 'user_sex', 'user_grade')
    search_fields = ('user_nanme',)


@admin.register(User_Info)
class UserInfo2(admin.ModelAdmin):
    pass


@admin.register(user_charge)
class UserInfo3(admin.ModelAdmin):
    pass
