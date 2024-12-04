from django.urls import path
from .views import CreatePostView, PostListView, PostViewSet



urlpatterns = [
    # 投稿作成用のエンドポイント (POST)
    path('create/', CreatePostView.as_view(), name='create-post'),
    
    # 投稿のUUID更新用のエンドポイント (POST)

    # 投稿リスト取得用のエンドポイント (GET)
    path('', PostListView.as_view(), name='post-list'),
    
    # 直近の投稿リスト取得用のエンドポイント (GET)
    path('SetGet/', PostViewSet.as_view(), name='pre_post-list'),
]
