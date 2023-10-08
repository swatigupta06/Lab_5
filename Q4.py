#Ques4
n = int(input("Enter the no.: "))
x = int(input("Enter no.: "))
count1 = 0
count2 =0
while x!=-999:
    if x%n == 0:
        count1 += 1
    else:
        count2 += 1
    x= int(input("Enter number: "))
print("no of divisible numbers: ", count1)
print("no of non divisible numbers: ", count2)
