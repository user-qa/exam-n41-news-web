from django.contrib import admin

from users.models import UserModel, ConfirmationCodeModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username','email','phone_number','date_of_birth',)
    search_fields = ('username','email','phone_number',)
    list_filter = ('username','email','phone_number',)


@admin.register(ConfirmationCodeModel)
class ConfirmationCodeModelAdmin(admin.ModelAdmin):
    list_display = ('code', 'email', 'created_at',)
    search_fields = ('code', 'email', 'created_at',)
    list_filter = ('code', 'email', 'created_at',)
