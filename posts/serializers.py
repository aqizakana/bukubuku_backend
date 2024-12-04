from rest_framework import serializers
from .models import Post
from analyze.charCount import charCount  # Ensure this import matches the location of your charCount function

class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = Post
        fields = ['id', 'username', 'content', 'createdAt', 'charCountResult', 'analyze8labelsResult','koheiduckSentimentScore','koheiduckSentimentLabel']
        read_only_fields = ['id', 'username', 'createdAt', 'charCountResult', 'analyze8labelsResult','koheiduckSentimentScore','koheiduckSentimentLabel']