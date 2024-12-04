from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from analyze.sentiment_analyze import analyze_sentiment_text
from analyze._8labels import analyze_8labels
from analyze.charCount import charCount
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer   
    
    permission_classes = [permissions.AllowAny]
    
    

    def perform_create(self, serializer):
        content = serializer.validated_data['content']  # 投稿の内容
        charCount_result = charCount(content)  # カウント結果
        sentiment_result = analyze_sentiment_text(content)  # 感情分析
        sentiment_score = sentiment_result[0]['score']
        sentiment_label = sentiment_result[0]['label']
        analyze_8labels_result = analyze_8labels(content)  # MLAskでの分析

        # Save post with additional data
        serializer.save(
            user=self.request.user,  # 投稿者
            charCountResult=charCount_result,  # 文字数結果
            koheiduckSentimentScore=sentiment_score,  # 感情スコア
            koheiduckSentimentLabel=sentiment_label,  # 感情ラベル
            analyze8labelsResult=analyze_8labels_result,  # 8ラベル分析
        )


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # 認証済みユーザーのみアクセス可能

class PostViewSet(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-createdAt')[:20]  # 直近20件の投稿を取得
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]  # 認証されていないユーザーもアクセス可能



