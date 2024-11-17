# Python 3.12のスリムなベースイメージを使用
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY . /app

# パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# main.pyを実行するコマンド
CMD ["python", "main.py"]
