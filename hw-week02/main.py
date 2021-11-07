from training import train_and_evaluate
from dataset import *

# train, evaluate and plot for every logical gate
train_and_evaluate(and_labels, "AND")
train_and_evaluate(or_labels, "OR")
train_and_evaluate(not_and_labels, "NAND")
train_and_evaluate(not_or_labels, "NOR")
train_and_evaluate(xor_labels, "XOR")
