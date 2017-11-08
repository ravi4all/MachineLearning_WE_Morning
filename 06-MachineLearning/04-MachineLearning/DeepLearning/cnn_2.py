from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


# Classification
classifier = Sequential()

# Convolutional Operation
classifier.add(Convolution2D(32,(3,3), activation='relu', input_shape = (64,64,3)))

# Max Pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))

# Flattening
classifier.add(Flatten())

# Fully connected
classifier.add(Dense(output_dim=128, activation='relu'))
classifier.add(Dense(output_dim = 1, activation='sigmoid'))


# Complie CNN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary')

model.fit_generator(
        train_generator,
        steps_per_epoch=8000,
        epochs=20,
        validation_data=validation_generator,
        validation_steps=200,
        nb_val_samples = 2000)