#!/bin/bash

# このスクリプトは、PyInstallerを使用してAIデスクトップアプリケーションの実行可能な.exeファイルを生成します。

# 必要なパッケージをインストール
pip install -r ../requirements.txt

# PyInstallerを使用してアプリケーションをビルド
pyinstaller --onefile --name ai_desktop_app ../src/main.py --specpath ../packaging

# ビルドが完了したら、distフォルダに生成された.exeファイルを確認してください。