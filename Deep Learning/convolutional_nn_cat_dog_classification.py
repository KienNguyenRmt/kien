import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import tensorflow as tf

physical_devices = tf.config.experimental.list_physical_devices('GPU')
try: 
  tf.config.experimental.set_memory_growth(physical_devices[0], True) 
except: 
  # Invalid device or cannot modify virtual devices once initialized. 
  pass 

#Part 1: Building the CNN
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
#convolution2D is used to process photos, 3D is used for video
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

#Initialize the CNN
classifier = Sequential()
#Add the convolution layer: This step is to create different Feature Detectors which then result in many Feature Maps
classifier.add(Convolution2D(filters=32, kernel_size=(3,3), input_shape=(64,64,3), activation='relu'))
#Max Pooling Layer: To reduce the size of Feature maps, therefore reduce the number of nodes in the fully connected ANN later
classifier.add(MaxPooling2D(pool_size=(2,2), strides=None))
#Adding the Second Convolutional layer
classifier.add(Convolution2D(filters=32, kernel_size=(3,3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2), strides=None))
#Flattening: Taking all out pool feature maps, and flatten it to a layers that contain all the single cells of our feature maps
classifier.add(Flatten())
#Full Connection
   # Add hidden layer
classifier.add(Dense(units=128, activation='relu'))
   # Add the output (activation = softmax if there are more than 2 output)
classifier.add(Dense(units=1, activation='sigmoid'))
#The number of unit 128 is an experienced pick in this case, given the number of nodes of flatten layer.
#Normally number of unit around 100 is fine, but its better to choose the power of 2, which is 128 in this case
# The Kernal Initializer = 'uniform' is only necessary in case of classic ANN, because we need random start there
#Compiling the CNN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#Fitting the CNN to the images
    # We need to run the Image Augmentation to enrich our photos training data (with different random algorithms like tilted photo.)
    # Therefore, we dont run into overfitting problem
    # Find more info here https://keras.io/preprocessing/image/

from tensorflow.keras.preprocessing.image import ImageDataGenerator    
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

trainning_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        trainning_set,
        steps_per_epoch=(8000/32),
        epochs=25,
        validation_data=test_set,
        validation_steps=(2000/32))

def test():
	photo = 'random_4.jpg'
	from PIL import Image  
	# creating a object  
	im = Image.open('dataset/random/' + photo)  
	im.show() 
	from tensorflow.keras.preprocessing import image
	# Replace codo_2.jpg by your image path
	test_image = image.load_img('dataset/random/' + photo, target_size = (64, 64))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = classifier.predict_classes(test_image)
	print(result)
	if result[0][0] == 1:

	    print("The image is a dog")
	else:
	 
	    print("The image is a cat")
