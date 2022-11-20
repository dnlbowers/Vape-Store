from django.db import models


# Create your models here.
class CustomerMessages(models.Model):

    CONTACT_REASON = (
        ('General Support', 'General Support'),
        ('Order', 'Order'),
        ('Product Info', 'Product Info'),
        ('Other', 'Other'),
    )

    date_received = models.DateTimeField(auto_now_add=True)
    name = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(null=False, blank=False, max_length=254)
    contact_reason = models.CharField(
        max_length=50, choices=CONTACT_REASON, default='General Support')
    subject = models.CharField(max_length=254)
    message = models.TextField(null=False, blank=False,)
    pending_reply = models.BooleanField(default=True)
    marked_as_done = models.BooleanField(default=False)

    def __str__(self):
        return f" message from {self.email}"


class InternalCommunicationNotes(models.Model):
    """
    Model to store internal notes for customer messages
    """
    related_message = models.ForeignKey(
        CustomerMessages,
        on_delete=models.CASCADE,
        related_name='related_message')
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return f'Internal notes for message id no. {self.related_message.id}'
