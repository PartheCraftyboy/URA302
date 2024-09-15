# 1
import random

for _ in range(100):
    length = random.randint(6, 8)
    string = ""
    for _ in range(length):
        string = string + chr(random.randint(97,122))
    print(string)

# 2
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in range(600, 801):
    if is_prime(number):
        print(number)

#3
for number in range(100, 1001):
    if number % 7 == 0 and number % 9 == 0:
        print(number)