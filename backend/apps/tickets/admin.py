from django.contrib import admin
from apps.tickets.models import Tickets, ImagesTicket

# Register your models here.


class ImagesTicketsInline(admin.TabularInline):
    '''Tabular Inline View for '''
    model = ImagesTicket
    min_num = 1
    max_num = 20
    extra = 0
    # raw_id_fields = (,)
    fieldsets = (
        (None, {
            "fields": (
                ('image'),
            ),
        }),
    )


@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'requesting_by', 'created', 'service', 'assigned_to')
    inlines = [ImagesTicketsInline,]
    fieldsets = (
        (None, {
            "fields": (
                ('requesting_by', 'assigned_to'),
                ('service', 'description')
            ),
        }),
    )
    readonly_fields = ('state',)


@admin.register(ImagesTicket)
class ImagesTicketAdmin(admin.ModelAdmin):
    list_display = ('image',)
