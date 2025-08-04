from django.contrib import admin
from .models import Member
from django.utils.html import format_html
from .constraints import MemberStatus
from django.contrib.auth.models import Group, User
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .custom_admin.field_sets import MemberFieldSets
from .custom_admin.display import MemeberDisplay
from .custom_admin.list_view import MemeberListView

admin.site.unregister(Group)
admin.site.unregister(User)




@admin.register(Member)
class MemberAdmin(MemeberListView, MemberFieldSets, MemeberDisplay, admin.ModelAdmin):
    pass
