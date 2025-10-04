# settings.py

# このファイルはアプリケーションの設定を管理します。

# モデルのパラメータ
MODEL_PARAMS = {
    'learning_rate': 0.001,
    'batch_size': 32,
    'num_epochs': 100,
}

# 環境設定
ENVIRONMENT = {
    'debug': True,
    'log_level': 'INFO',
    'api_endpoint': 'http://localhost:5000/api',
}

# その他の設定
OTHER_SETTINGS = {
    'max_input_length': 512,
    'output_format': 'json',
}