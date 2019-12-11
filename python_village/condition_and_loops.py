def sum_of_odd(a, b):
    sum = 0
    for i in range(a,b+1):
        if i % 2 != 0:
            sum +=i
    print(sum)

sum_of_odd(4277,8328)