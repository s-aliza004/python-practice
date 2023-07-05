from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME


greeting="Good morning,"
name="Aliza" 
print(type(name))
#concatenating two strings
c= greeting+name
print(c)

name="Aliza"
print(name[4])
print(name[0:2])
print(name[1:4])
print(name[:4])#is same as name[0:4]
print (name[0:])#is same as name [0:4]
print (name[1:])#is same as name [1:4]
print(name[-4:-1])#is same as name[1:4]

name="Helloworld"
d =name[ 0:9:3]
print(d)

