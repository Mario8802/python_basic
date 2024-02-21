from math import sqrt
number = int(input())
flag = 0
if number > 1:
    for k in range(2,int(sqrt(number + 1))):
        if number % k == 0:
            flag = 1
            break
        if flag == 0:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is Not a Prime number")
