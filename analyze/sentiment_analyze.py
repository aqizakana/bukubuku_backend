try:
    from transformers import pipeline
except ImportError as e:
    print(f"インポートエラー: {e}")
    raise

# モデルを明示的に指定
model_name = 'koheiduck/bert-japanese-finetuned-sentiment'
try:
    classifier = pipeline('sentiment-analysis', model=model_name)
    tokenizer_kwargs={"clean_up_tokenization_spaces": False}
except Exception as e:
    print(f"分類器の初期化エラー: {e}")
    raise

def analyze_sentiment_text(text):
    try:
  
        return classifier(text)
    except Exception as e:
        print(f"感情分析エラー: {e}")
        raise

