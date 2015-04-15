__author__ = 'gonzalosalazarvelasquez'

x0 = 1
x1 = 0
x2 = 0
y1 = 0

ta = 0.6

w0 = 1
w1 = 0
w2 = 0.5

net = x0 * w0 + x1 * w1 + x2 * w2
print(" net ", net )

error = y1 - net
print(error)

w0 = w0 + ta * error * x0
w1 = w1 + ta * error * x1
w2 = w2 + ta * error * x2

print(w0)
print(w1)
print(w2)