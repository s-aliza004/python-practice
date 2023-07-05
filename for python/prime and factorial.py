# num=int(input("Enter the number:\n"))
# prime = True
# for i in range(2,num):
#     if (num%i==0):
#         prime=False
#         break
# if prime:
#     print("this number is prime")
# else:
#     print("this number is not prime")


#n!=1 X 2 X 3 X 5 X 6......so on..
#5!= 1 X 2 X 3 X 4 X 5
num=int(input("Enter the number:\n"))
factorial=1
for i in range(1,num+1):
    factorial=factorial * i
print(f"the factorial of {num} is {factorial}")