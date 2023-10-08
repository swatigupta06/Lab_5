#Ques6
a = int(input("Enter a no.: "))
b = int(input("Enter another no.: "))
minimum = min(a,b)
i = 2
j = 1
while i>0:
    if i <= minimum:
        if a%i == 0 and b%i == 0:
            j = i
            print("LCM is", j)
            break
        else:
            i += 1
    else:
        print("LCM is",j)
        break
    