from django.contrib.auth.models import User
from django.db import models


class WebsiteDetail(models.Model):
    title = models.CharField(max_length=150)
    web_url = models.URLField()
    logo = models.ImageField(upload_to='sitelogos/')
    feature = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure only one website is marked as feature
        if self.feature:
            WebsiteDetail.objects.filter(feature=True).update(feature=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        ordering = ['order', 'title']


class ConfigDetail(models.Model):
    CONFIG_CHOICES = [
        ('PN', 'Push-Notification'),
        ('AM', 'Admob'),
    ]
    config_type = models.CharField(max_length=3, choices=CONFIG_CHOICES, default='PN')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



