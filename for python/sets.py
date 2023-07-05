a={1,2,5,3,1}
print(a)
print(type(a))


#important:this syntax will create an empty dictionary not an empty sets
a={}
print(type(a))

#An empty set can be created using the below syntax
b=set()
print(type(b))

#adding values  to an empty set
b.add(4)
b.add(34)
#b.add([2,3,7]) #cannot add list or dictionary to sets.
#b.add({3:6})
b.add((2,9,0)) #we can add tuple
print(b)

print(len(b)) #prints the length of the sets.
b.remove(4) #remove 4 from the set
print(b)
#b.remove(40) #throws an error brcause 40 is not present in the set
print(b)
print(b.pop()) #removes an arbitrary element from the set
print(b.clear())
