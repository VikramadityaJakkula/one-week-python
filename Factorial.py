def factorial(num):
    fact = 0
    if num == 0:
        return 1
    else:
        fact = num * factorial(num-1)
    return fact


num = 5
print("Factorial of",num,"is:",factorial(num))

