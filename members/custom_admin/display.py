from ..constraints import MemberStatus
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class MemeberDisplay:
    def status_badge(self, obj):
        """Display status as colored badges"""
        if obj.status == MemberStatus.ACTIVE:
            return format_html(
                '<span style="background-color: #28a745; color: white; padding: 4px 8px; '
                'border-radius: 4px; font-size: 11px; font-weight: bold;">{}</span>',
                _('Active')
            )
        elif obj.status == MemberStatus.EXPIRED:
            return format_html(
                '<span style="background-color: #dc3545; color: white; padding: 4px 8px; '
                'border-radius: 4px; font-size: 11px; font-weight: bold;">{}</span>',
                _('Expired')
            )
        else:
            return obj.get_status_display()
    
    status_badge.short_description = _('Status')
    status_badge.admin_order_field = 'status'

    def member_image(self, obj):
        """Display member image as a larger square thumbnail in list view"""
        if obj.photo:
            return format_html(
                '<img src="{}" style="height:64px;width:64px;object-fit:cover;border-radius:8px;" alt="Member Image"/>',
                obj.photo.url
            )
        return "-"
    member_image.short_description = _('Image')