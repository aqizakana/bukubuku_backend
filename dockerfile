FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 環境変数を設定
ENV DJANGO_SETTINGS_MODULE=my_api.settings.production 


# アプリケーションを実行
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]