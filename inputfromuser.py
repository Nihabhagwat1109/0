#input from user
n= int(input("how many numbers"))
lst=[]
for n in range (n):
    numbers= int(input("enter a number"))
    lst.append(numbers)
    print("sum of the numbers is:",sum(lst))