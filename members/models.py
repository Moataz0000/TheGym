from django.db import models
from django.utils.translation import gettext_lazy as _
from phonevalidatorGCC.fields import PhoneNumberField
from .constraints import MemberStatus, SubscriptionPeriod
from dateutil.relativedelta import relativedelta
from django.utils import timezone


class Member(models.Model):
    full_name = models.CharField(
        max_length=500,
        unique=True,
        verbose_name=_("Full Name")
    )
    age = models.PositiveIntegerField(verbose_name=_('Age'))
    phone_number = PhoneNumberField(
        country_code='EG',
        max_length=11,
        unique=True,
        help_text=_("Enter a valid Egyptian phone number."),
        verbose_name=_("Phone Number")
    )
    subscription_plan = models.CharField(
        max_length=20,
        choices=SubscriptionPeriod.choices,
        default=SubscriptionPeriod.ONE_MONTH,
        verbose_name=_("Subscription Plan")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        verbose_name=_("Price")
    )
    has_treadmale = models.BooleanField(
        verbose_name=_("Has Tread Male"),
        default=False
    )
    start_from = models.DateField(
        default=timezone.localdate,
        verbose_name=_("Start Date")
    )
    expiration_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Expiration Date")
    )
    status = models.CharField(
        max_length=25,
        choices=MemberStatus.choices,
        verbose_name=_("Status")
    )

    def save(self, *args, **kwargs):
        if not self.expiration_date:
            months = int(self.subscription_plan.replace('MONTH', ''))
            self.expiration_date = self.start_from + relativedelta(months=months)
        
        # Update status based on current date
        today = timezone.localdate()
        self.status = MemberStatus.ACTIVE if today <= self.expiration_date else MemberStatus.EXPIRED

        super().save(*args, **kwargs)


    def __str__(self):
        return self.full_name
    

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")