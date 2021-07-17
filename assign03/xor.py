import numpy as np
import matplotlib.pyplot as plt
import sys

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

num_inputs = 2
num_hiddenlayers = 2
num_outputs = 1

n = 0.1 # 0.001, 0.01 <- Magic values
reg_param = 0 # 0.001, 0.01 <- Magic values
max_iter = 10000 # 5000 <- Magic value
num_training_data = 4 # Number of training examples

np.random.seed(1)

W1 = np.random.randn(num_hiddenlayers,num_inputs)
W2 = np.random.randn(num_outputs,num_hiddenlayers)


B1 = np.random.randn(num_hiddenlayers, 1)
B2 = np.random.randn(num_outputs, 1)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))
    
    
def forward(X, j, _W1, _W2, _B1, _B2):
    a0 = X[j].reshape(X[j].shape[0], 1) # Getting the training example as a column vector.

    z1 = _W1.dot(a0) + _B1 # 2x2 * 2x1 + 2x1 = 2x1
    a1 = sigmoid(z1) # 2x1

    z2 = _W2.dot(a1) + _B2 # 1x2 * 2x1 + 1x1 = 1x1
    a2 = sigmoid(z2)

#     if predict: return a3
    return (a0, a1, a2)
    
    
def backward(X, y, j, a0, a1, a2, _W1, _W2, dW1, dW2, dB1, dB2):
    dz2 = a2 - y[j] # 1x1
    dW2 += dz2 * a1.T # 1x1 .* 1x2 = 1x2

    dz1 = np.multiply((_W2.T * dz2), sigmoid(a1)) # (2x1 * 1x1) .* 2x1 = 2x1
    dW1 += dz1.dot(a0.T) # 2x1 * 1x2 = 2x2

    dB1 += dz1 # 2x1
    dB2 += dz2 # 1x1
    
    return dW1, dW2, dB1, dB2
    
    
    
def calc_cost(c, y, j, a2):
    
    c = c + (-(y[j] * np.log(a2)) - ((1 - y[j]) * np.log(1 - a2)))
    
    return c
    
    
    

def train(_W1, _W2, _B1, _B2, X, y): # The arguments are to bypass UnboundLocalError error
    cost = np.zeros((max_iter, 1))
    
    for i in range(max_iter):
        c = 0
        
        dW1 = 0
        dW2 = 0

        dB1 = 0
        dB2 = 0
        
        for j in range(num_training_data):

            # Forward Prop.
            a0, a1, a2 = forward(X, j, _W1, _W2, _B1, _B2)

            # Back Prop.
            dW1, dW2, dB1, dB2 = backward(X, y, j, a0, a1, a2, _W1, _W2, dW1, dW2, dB1, dB2)

            # calculate cost
            c = calc_cost(c, y, j, a2)
        
        _W1 = _W1 - n * (dW1 / num_training_data) + ( (reg_param / num_training_data) * _W1)
        _W2 = _W2 - n * (dW2 / num_training_data) + ( (reg_param / num_training_data) * _W2)

        _B1 = _B1 - n * (dB1 / num_training_data)
        _B2 = _B2 - n * (dB2 / num_training_data)
        cost[i] = (c / num_training_data) + ( (reg_param / (2 * num_training_data)) * 
            (np.sum(np.power(_W1, 2)) + np.sum(np.power(_W2, 2))))
    return (_W1, _W2, _B1, _B2)
    
    
    
if __name__ == '__main__':

    W1, W2, B1, B2 = train(W1, W2, B1, B2, X, y)
    print(W1)
    print(W2)
    print(B1)
    print(B2)
    
    
