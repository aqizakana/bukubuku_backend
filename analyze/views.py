from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .sentiment_analyze import analyze_sentiment_text
from .charCount import charCount
""" from .ML_Ask import analyze_ml_ask
from .textBlob import NounPhrase """
from ._8labels import  analyze_8labels


import numpy as np

@csrf_exempt
@require_http_methods(["POST"])
def analyze_sentiment(request):
    try:
        data = json.loads(request.body)
        text = data.get('content')
        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)
        if len(text) > 512:
            text = text[:512]
        result = analyze_sentiment_text(text)
        return JsonResponse(result, safe=False)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except KeyError as e:
        return JsonResponse({"error": f"Missing key: {str(e)}"}, status=400)
    except Exception as e:
        print(f"Error: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def charCountView(request):
    try:
        data = json.loads(request.body)
        text = data.get('content')
        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)
        result = charCount(text)
        return JsonResponse(result, safe=False)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except KeyError as e:
        return JsonResponse({"error": f"Missing key: {str(e)}"}, status=400)
    except Exception as e:
        print(f"Error: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def analyze_8labels_views(request):
    try:
        data = json.loads(request.body)
        text = data.get('content')
        if not text:
            return JsonResponse({'error': 'テキストが提供されていません'}, status=400)
        
        result = analyze_8labels(text)
        print("API応答:", result)  # デバッグ用ログ
        return JsonResponse({'result': result}, safe=True)
    
    except json.JSONDecodeError:
        return JsonResponse({"error": "無効なJSONです"}, status=400)
    except KeyError as e:
        return JsonResponse({"error": f"キーが不足しています: {str(e)}"}, status=400)
    except Exception as e:
        print(f"エラー: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)
    

    

""" #textBlobを使った名詞抽出
@csrf_exempt
@require_http_methods(["POST"])
def extract_noun_phrases(request):
    try:
        data = json.loads(request.body)
        text = data.get('text')
        if not text:
            return JsonResponse({'error': 'テキストが提供されていません'}, status=400)
        result = NounPhrase(text)
        return JsonResponse(result, safe=False)

    except json.JSONDecodeError:
        return JsonResponse({"error": "無効なJSONです"}, status=400)
    except KeyError as e:
        return JsonResponse({"error": f"キーが不足しています: {str(e)}"}, status=400)
    except Exception as e:
        print(f"エラー: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500) """
    

    

    


