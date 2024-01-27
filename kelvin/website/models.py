from django.db import models
from datetime import datetime


# Create your models here.
class Concert(models.Model):
    status_choices = (
        ("OV", "Over"),
        ("FS", "For Sale"),
        ("UC", "Upcoming"),
        ("SO", "Sold Out"),
        ("NY", "Not Yet"),
    )
    Concert_Nickname = models.CharField(
        max_length=15,
        help_text="This is just a nickname for this concert to make it easier for you to distinguish in the admin page.",
        null=False,
        blank=False,
        default="Concert",
    )
    Concert_Status = models.CharField(max_length=2, choices=status_choices)
    Concert_Date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Concert_Nickname


class TicketType(models.Model):
    ticket_label = models.CharField(
        max_length=40,
        help_text="This will be the ticket name shown to the audience (i.e. 'Standard Seating' or 'Concession Seating' or 'Restricted View')",
    )
    for_concert = models.OneToOneField(
        Concert,
        help_text="Please select the matching concert here. Make sure this is selected or the ticket will not show.",
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    Ticket_ID = models.CharField(
        max_length=40,
        help_text="This will be the price ID supplied by STRIPE which you can obtain via the treasurer. Refer to the webmaster bible's payments section for more information",
    )
    Linked_Tickets = models.ManyToManyField(
        "TicketType",
        blank=True,
        help_text="This should auto-populate when saving as long as the STRIPE products and prices are set up correctly. If this does not happen it may be done manually here. However it is not recommended.",
    )

    def __str__(self):
        return self.ticket_label


class Ticket(models.Model):
    name = models.CharField(max_length=60)
