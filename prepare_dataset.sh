#!/bin/bash

rm cell_images/*/Thumbs.db
mkdir dataset
mv cell_images dataset/cell_images_train
mkdir dataset/cell_images_validation
mkdir dataset/cell_images_validation/Parasitized
mkdir dataset/cell_images_validation/Uninfected
shuf -n 1000 -e dataset/cell_images_train/Parasitized/* | xargs -i mv {} dataset/cell_images_validation/Parasitized/
shuf -n 1000 -e dataset/cell_images_train/Uninfected/* | xargs -i mv {} dataset/cell_images_validation/Uninfected/
