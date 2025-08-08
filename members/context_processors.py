
from .models import Member
from django.db.models import Sum
from django.contrib.auth.models import User

def admin_metrics(request):
    return {
        'total_members': Member.objects.count(),
        'total_admins': User.objects.count()
    }
