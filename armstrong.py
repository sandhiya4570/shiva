low = 100
uppe = 2000
# low = int(input("Enter low range: "))
# upp = int(input("Enter upp range: "))
for num in range(low, upp + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
