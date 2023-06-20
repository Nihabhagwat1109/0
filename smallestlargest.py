#smallest_largest
ls=[]
for i in range(5):
    num=int(input("enter the first number"))
    ls.append(num)
    ls.sort()
    print("smallest number is:",ls[-0])
    print("largest number is:",ls[-1])