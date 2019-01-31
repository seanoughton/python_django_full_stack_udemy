from django.contrib import admin
from . import models

# Register your models here.
#allows you to use the admin interface with ability to edit models on the same page as the parent model => group member => parent is Group
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
