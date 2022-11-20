from django.db import models


# Create your models here.
class CustomerMessages(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField()
    date_left = models.DateTimeField(auto_now_add=True)
    pending_reply = models.BooleanField(default=True)

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
