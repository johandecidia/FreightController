from django.contrib import admin
from .models import UploadedFile

# Register your models here.

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'file_type', 'uploaded_at', 'client_id', 'user')  # fields to display in list view
    search_fields = ('file',)  # fields to search
    list_filter = ('file_type', 'uploaded_at')  # filters sidebar


admin.site.register(UploadedFile, UploadedFileAdmin)