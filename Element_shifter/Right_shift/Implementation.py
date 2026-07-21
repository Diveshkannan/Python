def Rshift(Arr,n):
    length=len(Arr)
    List=[None]*length
    for i in range(length):
          tmp=((i+n)%(length))
          List[tmp]=Arr[i]
    Arr[:]=List
L=[10,20,30,40,12,11]
n=int(input("Number:"))
if (n<=0):
    print("Invalid input")
else:
    Lshift(L,n)
print(L)
    
     

