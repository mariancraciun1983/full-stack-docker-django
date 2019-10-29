from django.contrib import admin
from .models import UserEmailTemplate


@admin.register(UserEmailTemplate)
class UserEmailTemplateAdmin(admin.ModelAdmin):
    pass
