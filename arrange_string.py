str1 = "PYnAtivE"
upper=[]
lower=[]
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string="".join(lower + upper)
print(sorted_string)