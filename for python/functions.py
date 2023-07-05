def percent(marks):
    p=((marks[0] + marks[1]+marks[2] +marks[3])/400)*100
    return p
marks1=[45,33,34,12]
percentage1= percent (marks1)

marks2=[25,89,56,7]
percentage2= percent (marks2)
print(percentage1,percentage2)



def greet(name):
    print("Good day,"+name)

greet("Aliza")

def mysum(num1,num2):
    return num1+num2
s=mysum(6,7)
print(s)