import numpy as np

# 1. create a 5x5 numpy array with normal distributed random numbers (µ = 0, σ = 1)
temp = np.random.normal(size = (5,5), loc = 0, scale = 1)

# 2. replace all entries of this array with the original entry squared, only if the original entry larger than 0.09
for i in range(5):
    for j in range(5):
        if temp[i][j] > 0.09:
            temp[i][j] = (temp[i][j])**2

# 3. print the fourth column of this array
print(temp[:,3])