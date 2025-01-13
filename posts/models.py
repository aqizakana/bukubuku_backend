from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    
    charCountResult = models.IntegerField(null=True, blank=True)
    analyze8labelsResult = models.JSONField(null=True, blank=True)
    koheiduckSentimentScore = models.FloatField(null=True, blank=True)
    koheiduckSentimentLabel = models.CharField(max_length=20, null=True, blank=True)
    
    

    def __str__(self):
        return f"{self.user.username}:{self.user.username}: {self.content[:50]}..."

    class Meta:
        ordering = ['-createdAt']
