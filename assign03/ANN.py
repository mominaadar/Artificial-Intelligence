from __future__ import print_function
import pandas
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from tensorflow.keras.utils import to_categorical

seed = 7
split = 350
np.random.seed(seed)

data_set = np.genfromtxt('dataset.csv',delimiter = ',')
np.random.shuffle(data_set)

train,test = data_set[:split,:],data_set[split:,:] 

X,Y = train[:,:-1],train[:,-1]
Y = to_categorical(Y,10)

New_X, New_Y = test[:,:-1],test[:,-1]

New_Y = to_categorical(New_Y,10)
model = Sequential()

model.add(Dense(512, input_dim=10000, activation='tanh'))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer= 'adagrad', metrics=['accuracy'])

result = model.fit(X,Y,batch_size = 120, epochs = 20 ,verbose = 2,validation_data = (New_X, New_Y))

score = model.evaluate(New_X, New_Y,verbose = 0)
print("Test score:", score[0])
print("Test accuracy:",score[1])
