from rest_framework import serializers
from .models import Post
from analyze.charCount import charCount  # Ensure this import matches the location of your charCount function

class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')


    class Meta:
        model = Post
        fields = ['id','user_id', 'username', 'content', 'createdAt', 'charCountResult', 'analyze8labelsResult','koheiduckSentimentScore','koheiduckSentimentLabel']
        read_only_fields = ['id', 'user_id', 'username', 'createdAt', 'charCountResult', 'analyze8labelsResult','koheiduckSentimentScore','koheiduckSentimentLabel']