


class MemeberListView:
    list_display = (
        'full_name',
        'age',
        'phone_number',
        'subscription_plan',
        'price',
        'has_treadmale',
        'start_from',
        'expiration_date',
        'status_badge',
    )
    list_filter = (
        'status',
        'has_treadmale',

    )
    search_fields = (
        'full_name',
        'phone_number',
    )
    ordering = ('-start_from',)
    readonly_fields = (
        'expiration_date',
        'status',
    )
    list_display_links = ('full_name',)
    list_per_page = 25

