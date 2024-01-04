#Calculate the sum and average of the digits present in a string


str1 = "PYnative29@#8496"
sum=0
count=0

for num in str1:
    if num.isdigit():
        count +=1
        sum=sum + int(num)
average=sum/count
print("Sum=", sum, "Average=", average)