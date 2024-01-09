#Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'

digit="".join([i for i in str1 if i.isdigit()])
print(digit)
