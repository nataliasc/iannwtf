import numpy as np
from preparation import sigmoid, sigmoidprime

'''
single layer perceptron
'''
class Perceptron:
    def __init__(self, input_units):
        '''
        :param input_units: an int specifying how many weights are coming into the perceptron
        '''

        self.input_units = input_units
        self.alpha = 1 # learning rate
        self.weights = np.random.randn(input_units)
        self.bias = np.random.randn()

    def forward_step(self, inputs):
        '''
        computes the activation of the perceptron based on the given input, using sigmoid as the activation function
        :param inputs: a list of the inputs to the perceptron
        '''
        self.inputs = inputs
        activation = 0
        for i, input in enumerate(inputs):
            activation += self.weights[i] * input
        self.activation = sigmoid(activation + self.bias)
        return self.activation

    def update(self, delta):
        '''
        updates the parameters by computing the gradients for weights and bias from the error term δ
        :param delta: the error signal
        '''
        self.bias -= self.alpha * 1 * delta
        for i, input in enumerate(self.inputs):
            gradient_weight = delta * input
            self.weights[i] -= self.alpha * gradient_weight
