#!/bin/bash

# 檢查是否有輸入參數
if [ $# -eq 0 ]; then
    echo "請提供要產生的模型名稱,例如:tiny, tiny.en, base, base.en, small, small.en, medium, medium.en, large-v3"
    exit 1
fi

# 進入 whisper.cpp 目錄
cd whisper.cpp

# 根據輸入的參數產生對應的 CoreML 模型
for model in "$@"; do
    case $model in
        tiny|tiny.en|base|base.en|small|small.en|medium|medium.en|large-v3)
            ./models/generate-coreml-model.sh $model
            ;;
        *)
            echo "未知的模型名稱: $model"
            ;;
    esac
done