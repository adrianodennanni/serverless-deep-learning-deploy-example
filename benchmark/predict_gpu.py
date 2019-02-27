from numpy import asarray, argmax, argwhere, expand_dims
from PIL.Image import open as pil_open
import time
import base64
from base64 import b64encode, b64decode
from io import BytesIO
from os import environ

from tensorflow.keras.models import load_model

# Package in current directory


model = load_model('../trained_model_0.9700.h5')

with open("../example.png", "rb") as image_file:
    encoded_string = b64encode(image_file.read())

image_binary = pil_open(BytesIO(b64decode(encoded_string)))
image_binary = image_binary.resize([96, 96])

full_image_np = asarray(image_binary, dtype='float32')/255.
arr = []

BATCH_SIZE = 1

for i in range(BATCH_SIZE):
    arr.append(full_image_np)

full_image_np = asarray(arr, dtype='float32')

# Warm-up
model.predict(full_image_np)

start_time = int(round(time.time() * 1000))
for i in range(16384//BATCH_SIZE):
    model.predict(full_image_np)

print(f'{(int(round(time.time() * 1000))-start_time)/1000.0} seconds')
