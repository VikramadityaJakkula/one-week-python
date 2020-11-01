"""In mathematics, the Fibonacci numbers, commonly denoted Fn, 
form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones,
 starting from 0 and 1. That is, and. for n > 1.
"""

def fibanocci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibanocci(num-1)+fibanocci(num-2)
    
num = input("enter a number:")
n = int(num)
sum = 0
for i in range(1,n+1):
    sum = sum + fibanocci(i)
    print(fibanocci(i)," ")
print("sum of fibanocci num is :", sum)
