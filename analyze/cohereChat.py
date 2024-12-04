import torch
from transformers import AutoTokenizer, AutoModel

# モデルとトークナイザーをロード
model_name = 'tohoku-nlp/bert-base-japanese-v3'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def encode_sentence(sentence):
    # テキストをトークン化してテンソルに変換
    inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)

    # モデルに入力して出力を取得
    with torch.no_grad():  # 勾配計算を行わない
        outputs = model(**inputs)

    # [CLS]トークンに対応するベクトルを抽出（文全体のベクトル表現）
    cls_embedding = outputs.last_hidden_state[:, 0, :]
    
    return cls_embedding

# テスト文のベクトル化
sentence = "私は2023年に東京大学に行きました。"
vector = encode_sentence(sentence)

print(vector)
