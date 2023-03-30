def is_prime(number):
    check = True
    for i in range(2, int(number / 2) + 1):
        if (number % i == 0):
            check = False
            break
    if (check):
        return number
output = [ i for i in range(2,20) if (is_prime(i))]
print(output)