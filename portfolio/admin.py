

from django.contrib import admin
from .models import Project, Screenshot,ContactMessage,CV,ProfilePicture

class ScreenshotInline(admin.TabularInline):
    model = Screenshot
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title', 'tags')
    inlines = [ScreenshotInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Screenshot)
admin.site.register(ContactMessage)

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    
admin.site.register(ProfilePicture)

