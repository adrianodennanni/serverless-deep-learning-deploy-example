import sys
import tensorflow.lite as lite

# Pega o nome do modelo da linha de comando
if(len(sys.argv) != 2):
    print('Usage: python gen_tflite.py <batch_size>')
    sys.exit()
else:
    batch_size = sys.argv[1]

h5_file_name = './trained_model_0.9700.h5'

converter = lite.TFLiteConverter.from_keras_model_file(
    h5_file_name, input_shapes={
        'input_1': [batch_size, 96, 96, 3]
    })

tflite_model = converter.convert()
tflite_filename = './model.tflite'
open(tflite_filename, 'wb').write(tflite_model)

print('TFLite criado em ' + tflite_filename)
