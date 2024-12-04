from django.urls import path
from . import views
from .views import analyze_sentiment, charCountView, analyze_8labels_views
urlpatterns = [
    path('analyzeSentiment/', views.analyze_sentiment, name='analyze_sentiment'),
   path('charCountView/', views.charCountView, name='charCount'),
   path('analyze8labels/', views.analyze_8labels_views, name='analyze_8labels_views'),
]