import matplotlib.pyplot as plt
import numpy as np
import math

def relu(x):
    return max(0.0, x)

def sigmoid(x):
    return 1.0/(1.0 + math.exp(-x))

def tanh(x):
    return ((math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x)))

inputs = [x for x in range(-10, 10)]

outputs = [[],[],[]]
outputs[0] = [relu(x) for x in inputs]
outputs[1] = [sigmoid(x) for x in inputs]
outputs[2] = [tanh(x) for x in inputs]

fig, axs = plt.subplots(1,3, sharex=True)
axs[0].plot(inputs, outputs[0])
axs[0].set_ylim([-10,10])
axs[0].set_xlim([-10,10])
axs[0].grid()

axs[1].plot(inputs, outputs[1])
axs[1].set_ylim([-2,2])
axs[1].set_xlim([-10,10])
axs[1].grid()

axs[2].plot(inputs, outputs[2])
axs[2].set_ylim([-2,2])
axs[2].set_xlim([-10,10])
axs[2].grid()


plt.show()