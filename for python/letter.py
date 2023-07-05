letter='''Dear <|NAME|>,
Greetings from ABC software house.I am Glad to tell you about your interview and
You are selected!
'Nice to meet you!
GOOD LUCK!
Thanks and regards,
Owner
Date: <|DATE|>
'''
name = input("Enter Name:\n")
date = input("Enter Date:\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print (letter)