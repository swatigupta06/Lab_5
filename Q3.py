#Ques3
n = int(input("Enter number of lines: "))
i = 1
while i <= n:
    print("*"*i)
    i += 1


n = int(input("Enter number of lines: "))
i = 1
a = (2*n)-1
while i<=n:
    print(" "*a,"* "*i)
    i += 1
    a -= 2
    

n = int(input("Enter number of lines you want to print: "))
i = 1
a = 2*n-1
while i<=(2*n):
    print(" "*a,"* "*i)
    i += 2
    a -= 2

