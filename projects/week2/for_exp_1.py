import random
const = 1000
mu = 0
sigma = 1
random_numbers = []
for i in range(10):
    random_value = random.normalvariate(mu, sigma) * const
    random_value = int(random_value)
    random_numbers.append(random_value)
    print(random_value)
print()
for i in random_numbers:
    print(i+1)