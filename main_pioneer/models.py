from django.db import models
from django.utils import timezone

class Email(models.Model):
    """Email"""

    email = models.EmailField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    language_ru = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'


class Contact(models.Model):
    """Contact"""

    name = models.TextField(max_length=254, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.TextField(max_length=15, blank=True)
    company = models.TextField(max_length=100, blank=True)
    message = models.TextField(max_length=450, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Blog(models.Model):
    """Blog"""

    name = models.TextField(max_length=254, blank=True)
    main_text = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    url = models.SlugField(max_length=150, unique=True, blank=True)
    language_ru = models.BooleanField(default=True)
    date_ru = models.TextField()
    date_en = models.TextField()
    # tags =

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
