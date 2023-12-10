import random
r = random.randrange(0, 1000)
def is_prime(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
        if k <= 0:
            return True
        else:
            return False
print(r)
print(is_prime(r))