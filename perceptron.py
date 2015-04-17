learning_rate = 0.6
weights = [1, 0, 0.5]
training_set = [((1, 1, 1), 1),
                ((1, 1, 0), 0),
                ((1, 0, 1), 0),
                ((1, 0, 0), 0)]


def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))


# execute program
while True:
    print('-' * 60)
    error_count = 0

    for input_vector, desired_output in training_set:
        print(weights)

        result = dot_product(input_vector, weights)

        if result >= 0:
            result = 1
        else:
            result = 0

        error = desired_output - result

        if error != 0:
            error_count += 1

            for index, value in enumerate(input_vector):
                weights[index] += learning_rate * error * value

    if error_count == 0:
        break

flag = True
# validate

print("-" * 60)
print("verification")
print('-' * 60)
for input_vector, desired_output in training_set:
        print(weights)

        result = dot_product(input_vector, weights)

        if result >= 0:
            result = 1
        else:
            result = 0

        error = desired_output - result

        if error != 0:
            print("weight no correct :(")
            break
print("weight correct! :D")



