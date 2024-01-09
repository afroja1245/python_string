# Remove empty strings from a list of strings

#using for loop
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str1=[]
for x in str_list:
    if x :
        str1.append(x)
print(str1)

#using filter function
new_str_list = list(filter(None, str_list))
print(new_str_list)


