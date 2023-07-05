sub1=int(input("Enter first subject marks:\n"))
sub2=int(input("Enter second subject marks:\n"))
sub3=int(input("Enter third  subject marks:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one of the subject")

elif(sub1 + sub2 +sub3)/3<40:
    print("you are fail due to total percentage less than 40")

else:
    print("congrtulations! you passed the exam")

