from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('vacancy', 'Vacancy'),
        ('result', 'Result'),
        ('exam', 'Exam Date'),
        ('admit_card', 'Admit Card'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# For email notifications
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
