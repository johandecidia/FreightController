from django.contrib import admin
from .models import Agent

# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'identifiers', 'created_at', 'updated_at']
    search_fields = ['name', 'code', 'identifiers']


admin.site.register(Agent, AgentAdmin)
