this = "   Ahmed is a good    "
print(this)
print(this.strip())

def remove_and_split(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = " Ahmed is a good   "
n=remove_and_split(this,"Ahmed")
print(n)
