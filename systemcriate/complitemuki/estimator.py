from typing_extensions import Self
import numpy as np
import tflite_runtime.interpreter as tflite
import cv2
from util import estimateimage

model_path="/home/raspberry/Desktop/myenv/program/mukiver1.tflite"
image_path=''
dsize=(50,50)

# TFLiteモデルの読み込み
interpreter = tflite.Interpreter(model_path=model_path)

# メモリ確保。これはモデル読み込み直後に必須
interpreter.allocate_tensors()

# 学習モデルの入力層・出力層のプロパティをGet.
input_details = inter.get_input_details()
output_details = inter.get_output_details()
#print(input_details)
#print(output_details)

# 入力層のテンソルデータ構成の取得
input_shape = input_details[0]['shape']

#入力画像を読み込み、編集
input_data=estimateimage(image_path,dsize)

# indexにテンソルデータのポインタをセット
interpreter.set_tensor(input_details[0]['index'], input_data)

# 推論実行
interpreter.invoke()

# 推論結果は、output_detailsのindexに保存されている
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
