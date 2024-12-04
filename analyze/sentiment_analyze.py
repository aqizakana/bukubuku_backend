try:
    from transformers import pipeline
    import numpy as np
except ImportError as e:
    print(f"インポートエラー: {e}")
    raise

# モデルを明示的に指定
model_name = 'koheiduck/bert-japanese-finetuned-sentiment'
try:
    classifier = pipeline('sentiment-analysis', model=model_name)
except Exception as e:
    print(f"分類器の初期化エラー: {e}")
    raise

def analyze_sentiment_text(text):
    try:
  
        return classifier(text)
    except Exception as e:
        print(f"感情分析エラー: {e}")
        raise

""" text = '夕食がとても美味しく友達も喜んでいました。ありがとうございます！客室担当方はフレンドリーで丁寧に接客してくれました。朝ご飯もちょうどいいくらいの量で満足でした。部屋も予想よりも広くびっくりしました。'
print(analyze_sentiment_text(text)) """