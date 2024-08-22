#!/bin/bash

# 檢查是否有輸入參數
if [ $# -eq 0 ]; then
    echo "請提供要下載的模型名稱,例如:tiny-q5_1, tiny.en-q5_1, base-q5_1, base.en-q5_1, small-q5_1, small.en-q5_1, medium-q5_0, medium.en-q5_0, large-v3-q5_0"
    exit 1
fi

# 進入 whisper.cpp 目錄
cd whisper.cpp

# 根據輸入的參數下載對應的模型
for model in "$@"; do
    case $model in
        tiny-q5_1|tiny.en-q5_1|base-q5_1|base.en-q5_1|small-q5_1|small.en-q5_1|medium-q5_0|medium.en-q5_0|large-v3-q5_0)
            ./models/download-ggml-model.sh $model
            ;;
        *)
            echo "未知的模型名稱: $model"
            ;;
    esac
done