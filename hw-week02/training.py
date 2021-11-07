import numpy as np
import matplotlib.pyplot as plt
from MLP import MLP
from perceptron import Perceptron
from dataset import *

def train_and_evaluate(labels, title_plot):
    '''

    :param labels:
    :return:
    '''
    mlp = MLP()
    nepochs = 1000
    labels = labels.reshape((4, 1))

    loss_avg = []
    accuracy_avg = []

    # train the instance for 1000 epochs
    for epoch in range(nepochs):
        losses = 0
        correct = 0  # number of correct predictions in this epoch

        # iterate through the training samples
        for x1, x2, target in np.concatenate((input_pairs, labels), axis=1):
            pred = mlp.forward_step([x1, x2])
            mlp.backprop_step(target)

            # loss function: Mean Squared Error (MSE)

            loss = (pred - target) ** 2
            losses += loss

            if round(pred) == target:
                correct += 1

        # compute and save average loss and accuracy of epoch
        accuracy = correct / len(input_pairs)
        loss = losses / len(input_pairs)
        loss_avg.append(loss)
        accuracy_avg.append(accuracy)

    # Create and show the plot
    x = range(nepochs)
    plt.plot(x, accuracy_avg, label="Accuracy")
    plt.plot(x, loss_avg, label="Loss")
    plt.title(title_plot)
    plt.legend()
    plt.show()

