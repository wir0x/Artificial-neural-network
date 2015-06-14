import random
import logging

log = logging


def random_weight(iteration):
    v = []
    for i in range(iteration):
        v.append(random.uniform(-2, 2))
    return v


def random_factor_learning():
    return random.uniform(0.2, 0.9)


def get_product_vectors(v1, v2):
    result = []
    for i in range(len(v2)):
        result.append(v1[i] * v2[i])
    return result


def get_sum_product_vectors(v1, v2):
    if not v1 or not v2:
        log.warning("vector is empty")
    return sum(get_product_vectors(v1, v2))


def re_calculate_weight(vw, learning, error, vx):
    new_w = []
    for i in range(len(vw)):
        new_w.append(vw[i] + learning * error * vx[i])
    return new_w


def find_error(y, net_i):
    return y - net_i


def find_net_i(vw, vx):
    return 1 if get_sum_product_vectors(vw, vx) > 0 else 0


