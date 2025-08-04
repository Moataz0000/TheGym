from django.db import models
from django.utils.translation import gettext_lazy as _



class MemberStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', _("Active")
    EXPIRED = 'EXPIRED', _("Expired")



class SubscriptionPeriod(models.TextChoices):
    ONE_MONTH = '1MONTH', _("1 Month")
    TWO_MONTH = '2MONTH', _("2 Months")
    THREE_MONTH = '3MONTH', _("3 Months")
    FOUR_MONTH = '4MONTH', _("4 Months")
    FIVE_MONTH = '5MONTH', _("5 Months")
    SIX_MONTH = '6MONTH', _("6 Months")
    SEVEN_MONTH = '7MONTH', _("7 Months")
    EIGHT_MONTH = '8MONTH', _("8 Months")
    NINE_MONTH = '9MONTH', _("9 Months")
    TEN_MONTH = '10MONTH', _("10 Months")
    ELEVEN_MONTH = '11MONTH', _("11 Months")
    TWELVE_MONTH = '12MONTH', _("12 Months")