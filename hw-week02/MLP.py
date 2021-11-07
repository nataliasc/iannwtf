import numpy as np
from perceptron import Perceptron
from preparation import sigmoidprime

'''
multi-layer perceptron
'''
class MLP:
    # initializer
    def __init__(self):
        '''
        initialize a multi-layer perceptron with 1 hidden layer (4 perceptrons) and 1 output neuron
        :param input_units: an int specifying the number of inputs to the hidden layer
        '''
        self.hidden_layer = [Perceptron(2) for i in range(4)]
        self.output_neuron = Perceptron(4)
        self.output = None

    def forward_step(self, inputs):
        '''
        pass the inputs through the network
        :param inputs: a list of the inputs to the network
        '''
        # compute the activations for the hidden layer
        self.hidden_output = []
        for perceptron in self.hidden_layer:
            self.hidden_output.append(perceptron.forward_step(inputs))

        # feed the activations into the output neuron to compute the output
        self.output = self.output_neuron.forward_step(self.hidden_output)

        return self.output


    def backprop_step(self, target):
        '''
        update the parameters of the network
        :param target: yhat / the target of our network
        '''
        # compute the error signal of the neuron in the output layer
        delta_output = - (target - self.output) * sigmoidprime(self.output)

        # update bias & weights of the neurons in the hidden layer
        for i, perceptron in enumerate(self.hidden_layer):
            delta = delta_output * self.output_neuron.weights[i] * sigmoidprime(perceptron.activation)
            perceptron.update(delta)

        # update bias & weights of the output neuron
        self.output_neuron.update(delta_output)
