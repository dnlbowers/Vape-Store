from django.contrib import admin
from .models import CustomerMessages, InternalCommunicationNotes


class InternalCommunicationNotesAdmin(admin.StackedInline):
    model = InternalCommunicationNotes
    extra = 1
    verbose_name_plural = 'Internal Communication Notes'
    verbose_name = 'Internal Communication Note'
    fields = ('notes', 'date',)
    readonly_fields = ('date',)
    can_delete = False


@admin.register(CustomerMessages)
class CustomerMessagesAdmin(admin.ModelAdmin):
    inlines = (InternalCommunicationNotesAdmin,)
    baseModel = CustomerMessages
    list_display = (
        'date_received',
        'name',
        'email',
        'subject',
        'pending_reply',
        'marked_as_done',
    )
    list_filter = ('pending_reply', 'marked_as_done', 'date_received')
    summer_note_field = ('message',)
    readonly_fields = ('date_received', 'message',)

    ordering = ('-date_received',)
