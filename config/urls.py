
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns



from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class GymAdminSite(admin.AdminSite):
    site_header = "The Gym Admin"

    def index(self, request, extra_context=None):
        # prepare your data
        total_users    = User.objects.count()

        

        extra = {
            'total_users':    total_users,
        }
        return super().index(request, extra_context=extra)


# instantiate and hook in urls.py instead of the default `admin.site`
gym_admin = GymAdminSite(name='gym_admin')


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),                 
)