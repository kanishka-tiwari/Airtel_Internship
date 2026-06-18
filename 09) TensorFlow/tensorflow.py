import tensorflow as tf
from tensorflow.keras import layers, models                         #define architecture and make a trainable structure  

mnist = tf.keras.datasets.mnist                                     #builtin dataset

(x_train, y_train), (x_test, y_test) = mnist.load_data()            #data to train and test AI model
x_train, x_test = x_train / 255.0, x_test / 255.0                   #normalise pixel values to make learning faster

model = models.Sequential([                                         #make a stack of layers
    layers.Flatten(input_shape=(28, 28)),                           #convert 2D array into 1D array
    layers.Dense(128, activation='relu'),                           #connection of layers which convert negative numbers into zeros
    layers.Dense(10, activation='softmax')                          #final output where connection with the highest probability is the answer
])

model.compile( 
    optimizer='adam',                                               #update the model according to the errors made
    loss='sparse_categorical_crossentropy',                         #compares how wrong the answer is to the data
    metrics=['accuracy']                                            #display percentage of images evaluated 
)

model.fit(x_train, y_train, epochs=5)                               #go through the entire dataset 5 times

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)     #test the model on unseen images 
print(f"\nFinal Test Accuracy: {test_acc * 100:.2f}%")              #quantify the final output 