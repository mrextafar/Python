def power2(n):
    if n == 2 or n == 1:
        return True
    elif n % 2 == 0:
        return power2(n // 2)
    else:
        return False
print(power2(10))