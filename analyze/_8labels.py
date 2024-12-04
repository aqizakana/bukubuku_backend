from transformers import AutoTokenizer, AutoModelForSequenceClassification, LukeConfig
import torch

# モデルとトークナイザーの初期化
tokenizer = AutoTokenizer.from_pretrained("Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime")
config = LukeConfig.from_pretrained('Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime', output_hidden_states=True)
model = AutoModelForSequenceClassification.from_pretrained('Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime', config=config)

def analyze_8labels(text):
    try:
        max_seq_length = 512
        token = tokenizer(text, truncation=True, max_length=max_seq_length, padding="max_length")
        output = model(torch.tensor(token['input_ids']).unsqueeze(0), torch.tensor(token['attention_mask']).unsqueeze(0))
        max_index = torch.argmax(torch.tensor(output.logits))

        sentiments = ['joy、うれしい', 'sadness、悲しい', 'anticipation、期待', 'surprise、驚き', 'anger、怒り', 'fear、恐れ', 'disgust、嫌悪', 'trust、信頼']
        return {"sentiment": sentiments[max_index]}
    except Exception as e:
        print(f"感情分析エラー: {e}")
        return {"error": str(e)}

