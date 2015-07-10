import random
import math
import numpy as np


def random_weight(number_iteration, range1, range2):
    """ Random weight"""
    v = []
    for i in range(number_iteration):
        v.append(random.uniform(range1, range2))
    return v


def random_learning_factor(range1, range2):
    """random_learning_factor 0.2 or 0.9"""
    return random.uniform(range1, range2)


def net_values(weights, vector):
    return sum(weights * vector)


def output_hidden_layer(net_x):
    return 1 / (1 + math.exp(-net_x))


def calculate_error_outputs(desired_output, obtained_output):
    return (desired_output - obtained_output) * output_hidden_layer(obtained_output)


def calculate_error_hidden(net_x, error_outputs, weights):
    """calculate_error_hidden"""
    return output_hidden_layer(net_x) * net_values(weights, error_outputs)


def recalculate_weight(weights, learning, error_x):
    """recalculate_weight"""
    new_weights = []
    for i in range(len(weights)):
        new_weights.append(weights[i] + (learning * error_x))
    return new_weights


# ----------------------------------------------------
weights_1 = np.array([-0.2, 0.1, 0.1])
learn = 0.5
error = -0.04
step8 = recalculate_weight(weights_1, learn, error)
print("step8->", step8)
# ----------------------------------------------------


# ----------------------------------------------------
error_outputs = np.array([0.4, 0.48])
weights1 = np.array([-0.2, 0])
weights2 = np.array([0.1, 0.2])
weights3 = np.array([-0.2, -0.1])
step7 = calculate_error_hidden(-0.1, error_outputs, weights3)
# print(step7)
# -------------------------------------------------------

weights_test = np.array([-0.2, 0.52, -0.2])
v0 = np.array([0.47, 0.52, 0.47])
v1 = np.array([1, 0, 1])
v2 = np.array([0, 1, 1])
v3 = np.array([1, 0, 0])

net_a = net_values(weights_test, v1)
output_net_a = output_hidden_layer(net_a)

# print(net_a, output_net_a)
# print(output_hidden_layer(0.4))
# print(calculate_error_outputs(0, 0.48))
