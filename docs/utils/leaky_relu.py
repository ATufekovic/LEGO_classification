import matplotlib.pyplot as plt
import numpy as np
import math

def leaky_relu(a, x):
    if x < 0:
        return x*a
    else:
        return x

inputs = [x for x in range(-10, 10)]

outputs = [leaky_relu(0.5, x) for x in inputs]


plt.plot(inputs, outputs)
plt.grid(b=True, which="major")
plt.show()