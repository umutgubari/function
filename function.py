def is_prime(number):
    if number < 2:
        print(f"{number} is not a prime number.")
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return False
    print(f"{number} is a prime number.")
    return True

#is_prime(113)
#is_prime(111)