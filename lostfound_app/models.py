from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    POST_TYPES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=5, choices=POST_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_post_type_display()}: {self.title}"
