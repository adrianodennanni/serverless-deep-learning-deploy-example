from tensorflow.keras import Model
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard, ReduceLROnPlateau, EarlyStopping
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Constants
BATCH_SIZE = 32
MAX_EPOCHS = 100

# Generators
train_generator = ImageDataGenerator(
    data_format='channels_last',
    rescale=1. / 255,
    # rotation_range=40,
    # horizontal_flip=True,
    # vertical_flip=True
)

train_batches = train_generator.flow_from_directory(
    batch_size=BATCH_SIZE,
    directory='dataset/cell_images_train',
    target_size=[96, 96],
    class_mode='categorical'
)


val_generator = ImageDataGenerator(
    data_format='channels_last',
    rescale=1. / 255
)

val_batches = train_generator.flow_from_directory(
    batch_size=BATCH_SIZE,
    directory='dataset/cell_images_validation',
    target_size=[96, 96],
    class_mode='categorical'
)

model = MobileNetV2(input_shape=(96, 96, 3),
                    weights='imagenet', include_top=False, classes=2)
flat = Flatten()(model.output)
output = Dense(2, activation='softmax')(flat)
model = Model(inputs=model.input, outputs=output)

# Prepare model to run
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy']
              )

# Callback to save weights, based on val_acc
model_checkpoint_callback = ModelCheckpoint(
    './checkpoints/{epoch:02d}_{val_acc:.4f}.h5',
    save_weights_only=False,
    verbose=1,
    monitor='val_acc',
    save_best_only=True,
    mode='max'
)

# Callbackto plot data on TensorBoard
tensorboard_callback = TensorBoard(
    log_dir='./logs/malaria',
    histogram_freq=0,
    batch_size=BATCH_SIZE
)

# Callback to reduce learning rate after plateaus
reduce_lr_callback = ReduceLROnPlateau(
    monitor='val_acc',
    factor=0.5,
    patience=6,
    min_lr=1e-6
)

early_stopping_callback = EarlyStopping(
    monitor='val_acc',
    patience=30,
    mode='max',
)

# Starts training the model
model.fit_generator(train_batches,
                    epochs=MAX_EPOCHS,
                    verbose=1,
                    validation_data=val_batches,
                    callbacks=[model_checkpoint_callback, tensorboard_callback,
                               reduce_lr_callback, early_stopping_callback]
                    )
