# Python packages
from base64 import b64decode
from io import BytesIO

# Packages from pip
from numpy import asarray, expand_dims
from PIL.Image import open

# Package in current directory
from tensorflow.lite.python.interpreter import Interpreter

INTERPRETER = Interpreter(model_path='./model.tflite')
INTERPRETER.allocate_tensors()

INPUT_DETAILS  = INTERPRETER.get_input_details()
OUTPUT_DETAILS = INTERPRETER.get_output_details()


def inference(request):
  image_binary = open(BytesIO(b64decode(request.form['image_base64'])))

  image_binary = image_binary.resize([96, 96])

  full_image_np = expand_dims(asarray(image_binary, dtype='float32')/255., axis=0)

  INTERPRETER.set_tensor(INPUT_DETAILS[0]['index'], full_image_np)
  INTERPRETER.invoke()

  for od in OUTPUT_DETAILS:
    for tensor in INTERPRETER.get_tensor(od['index']).tolist():
      return str({'Parasitized': tensor[0], 'Uninfected': tensor[1]})
