import numpy as np

# inputs to the logical gates of our network
input_pairs = np.array([[0, 0],
                        [0, 1],
                        [1, 0],
                        [1, 1]])

# labels (= true solution) for each gate, corresponding to the input pairs
and_labels = np.array([0, 0, 0, 1]) # logical AND
or_labels = np.array([0, 1, 1, 1]) # logical OR
not_and_labels = np.array([1, 1, 1, 0]) # logical NOT AND
not_or_labels = np.array([1, 0, 0, 0]) # logical NOT OR
xor_labels = np.array([0, 1, 1, 0]) # logical XOR
