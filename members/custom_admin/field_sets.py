from django.utils.translation import gettext_lazy as _



class MemberFieldSets:
    def get_fieldsets(self, request, obj=None):
        if obj:  
            return (
                (_('Personal Info'), {
                    'fields': (
                        'full_name',
                        'photo',
                        'age',
                        'phone_number',
                    )
                }),
                (_('Subscription Details'), {
                    'fields': (
                        'subscription_plan',
                        'price',
                        'start_from',
                        'expiration_date',
                        'status',
                    )
                }),
                (_('Facilities'), {
                    'fields': (
                        'has_treadmale',
                                                'notes'

                    )
                }),
            )
        else: 
            return (
                (_('Personal Info'), {
                    'fields': (
                        'photo',
                        'full_name',
                        'age',
                        'phone_number',
                        
                    )
                }),
                (_('Subscription Details'), {
                    'fields': (
                        'subscription_plan',
                        'price',
                        'start_from',
                    )
                }),
                (_('Facilities'), {
                    'fields': (
                        'has_treadmale',
                        'notes'
                    )
                }),
            )
