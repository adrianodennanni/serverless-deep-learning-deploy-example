from numpy import asarray, argmax, argwhere, expand_dims
from PIL.Image import open as pil_open
import time
import base64
from base64 import b64encode, b64decode
from io import BytesIO
from os import environ

# Package in current directory
from tensorflow.lite.python.interpreter import Interpreter

INTERPRETER = Interpreter(model_path='../../model.tflite')
INTERPRETER.allocate_tensors()

INPUT_DETAILS  = INTERPRETER.get_input_details()
OUTPUT_DETAILS = INTERPRETER.get_output_details()

with open("../../example.png", "rb") as image_file:
    encoded_string = b64encode(image_file.read())

start_time = int(round(time.time() * 1000))
for i in range(16384):
    image_binary = pil_open(BytesIO(b64decode(encoded_string)))
    image_binary = image_binary.resize([96, 96])

    full_image_np = expand_dims(asarray(image_binary, dtype='float32'), axis=0)/255.

    INTERPRETER.set_tensor(INPUT_DETAILS[0]['index'], full_image_np)
    INTERPRETER.invoke()

    output_data = []
    for od in OUTPUT_DETAILS:
        for tensor in INTERPRETER.get_tensor(od['index']).tolist():
            output_data.append(tensor)

print(f'{(int(round(time.time() * 1000))-start_time)/1000.0} seconds')
