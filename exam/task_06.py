number = int(input())
counter_num = 0
flag = False
for a in range(1, 9, + 1):
    for b in range(9, a, - 1):
        for c in range(0, 9, + 1):
            for d in range(9, c, - 1):
                sum_num = (a + b + c + d)
                multiple_sum = (a * b * c * c)

                if sum_num == multiple_sum and number % 10 == 5:
                    counter_num += 1
                    print(str(a)+str(b)+str(c)+str(d))
                    flag = True
                    break

                elif multiple_sum // sum_num == 3 and number % 3 == 0:
                    counter_num += 1
                    print(str(d) + str(c) + str(b) + str(a))
                    flag = True
                    break

            if flag:
               break
        if flag:
            break
    if flag:
       break

if counter_num == 0:

    print("Nothing found")



