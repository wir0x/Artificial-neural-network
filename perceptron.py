import random

vc = [[1, 0, 0],
      [1, 0, 1],
      [1, 1, 0],
      [1, 1, 1]]

y = [0, 1, 1, 1]
w = [1, 0, 0.5]
learn = 0.6


def weight_random(vector):
    pesos = []
    for i in range(len(vector)):
        pesos.append(random.uniform(-2, 2))
    return pesos


def formula(vector):
    temp_v = []
    for i in range(len(vector)):
        temp_v.append(vector[i] * w[i])
    return sum(temp_v)


def recalculate_weight(e, x):
    for i in range(len(w)):
        w[i] += learn * e * x[i]


def validate_simple_perceptron(v):
    print("*" * 50 + "\n validate simple perceptron")
    for i in range(len(v)):
        net.append(formula(v[i]))
        _error = y[i] - 1 if net[i] > 0 else 0

        if _error != 0:
            return False
    return True


count = 0
while len(vc) > count:
    net = []
    print("-" * 50)

    for i in range(len(vc)):
        print(w)

        net.append(formula(vc[i]))

        result = 1 if net[i] > 0 else 0
        error = y[i] - result

        if error == 0:
            count += 1

        else:
            recalculate_weight(error, vc[i])
            count = 0

print("ok" if validate_simple_perceptron(vc) else "bad")
