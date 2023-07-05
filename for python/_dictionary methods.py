my_dic ={
    "Fast":"In a Quick Manner",
    "Change": "convert",
    "Marks" :[1,3,5,7],
    "anotherdic":{"Excuse":"Sorry"},
     1: 2
}
print(my_dic.keys()) #print the keys of dictionary
print(type(my_dic.keys())) # type is always as "dic_keys"
print(list(my_dic.keys())) #this type can be changed in list type
print(my_dic.values()) #print the values of the dict
print(my_dic.items())  #print the keys and values of the dict

Updatedict={
    "maryam":"friend",
    "best"  :"loyal"
}
my_dic.update(Updatedict) #update the dict by adding key-values pairs from update.dict
print(my_dic)

print(my_dic.get("Change")) # prints value associated with key "change".
print(my_dic["Change"])  # prints value associated with key "change".

#the differnece between .get and [] syntax in dictionaries?
print(my_dic.get("Change2")) #returns none as change2 is not present in the dictionary 
print(my_dic["Change2"])  # throws an error as change2 is not present in the dictionary