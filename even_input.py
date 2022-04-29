num1 = int(input("enter any num="))
num2 = int(input("enter any num="))
num3 = int(input("enter any num="))
num4 = int(input("enter any num="))
num5 = int(input("enter any num="))

l = [num1,num2,num3,num4,num5]
print(l)
i=0
while i<len(l):
    if l[i]%2==0:
        print("even",l[i])
    i+=1