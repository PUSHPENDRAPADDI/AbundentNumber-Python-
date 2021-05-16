num = int(input("Enter number for checking number is abundent or not = "))
sum=0
for i in range(1,num//2+1):
    if num % i == 0:
        sum = sum + i
if sum > num:
    print("Number is Abundent")
else:
    print("Number is not Abundent")