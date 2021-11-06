import numpy as np
from perceptron import Perceptron
from preparation import sigmoidprime

'''
multi-layer perceptron
'''
class MLP:
    # initializer
    def __init__(self, input_units):
        '''
        initialize a multi-layer perceptron with 1 hidden layer (4 perceptrons) and 1 output neuron
        :param input_units: an int specifying the number of inputs to the hidden layer
        '''
        self.hidden_layer = [Perceptron(input_units),
                             Perceptron(input_units),
                             Perceptron(input_units),
                             Perceptron(input_units)]
        self.output_neuron = Perceptron(4)
        self.output = None

    def forward_step(self, inputs):
        '''
        pass the inputs through the network
        :param inputs: a list of the inputs to the network
        '''
        # compute the activations for the hidden layer
        activations = []
        for perceptron in self.hidden_layer:
            activations.append(perceptron.forward_step(inputs))

        # feed the activations into the output neuron to compute the output
        self.output = self.output_neuron.forward_step(activations)


    def backprop_step(self, target):
        '''
        update the parameters of the network
        :param target: yhat / the target of our network
        '''
        # compute the error signal
        delta = - (target - self.output) * sigmoidprime(self.output)

        # update bias & weights of the output neuron
        self.output_neuron.update(delta)

        # update bias & weights of the neurons in the hidden layer
        for perceptron in self.hidden_layer:
            perceptron.update(delta)
