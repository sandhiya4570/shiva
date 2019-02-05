num = int(input("Enter any num: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime num")
            break
    else:
        print(num, "is a prime num")
else:
    print(num, "is not a prime num")
