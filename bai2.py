def factorials(number):
    output = 1
    for i in range(2, number + 1):
        output *= i
        return output
output = [factorials(i) for i in range(2,8)]
print(output)