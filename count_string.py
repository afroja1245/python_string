str1 = "P@#yn26at^&i5ve"
alpha=0
digit=0
symbol=0
for char in str1:
    if char.isdigit():
        digit=digit+1

    elif char.isalpha():
        alpha=alpha+1
    else:
        symbol=symbol+1

print("Chars =", alpha,"Digit=",digit,"Symbol =", symbol)

