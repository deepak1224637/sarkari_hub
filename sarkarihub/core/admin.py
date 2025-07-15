from django.core.mail import send_mail
from django.conf import settings
from django.contrib import admin
from .models import Post, Subscriber

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'link', 'description')
        }),
        ('Meta', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Only send notification for new posts, not edits
        if not change:
            from .models import Subscriber
            subscribers = Subscriber.objects.values_list('email', flat=True)
            if subscribers:
                subject = f"New {obj.get_category_display()} Posted: {obj.title}"
                message = f"A new {obj.get_category_display()} has been posted on SarkariHub.\n\nTitle: {obj.title}\n\nDetails: {obj.description}\n\nView: {obj.link}"
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    list(subscribers),
                    fail_silently=True,
                )

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    ordering = ('-subscribed_at',)
