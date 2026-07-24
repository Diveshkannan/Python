#recreated pop() from python in my version
def my_pop(re_list,length,index):
    if length==0:
        return 1
    if index>length-1 or index<-(length):
        return 1
    #store removing value
    value=re_list[index]
    #without refreshing the list,assign it
    temp=[None]*(length-1)
    if index>=0:
        location=0
        for i in range(length):
                if i!=index:
                     temp[location]=re_list[i]
                     location+=1
    else:
            for i in range(-1,-(length),-1):
                    location=0
                    if i!=index:
                        temp[location]=re_list[i]
                        location+=1
        
    #assign it
                        
    List_one[:]=temp
    
    return value

len_one=int(input("Length of your list:"))

List_one=[None]*len_one
for i in range(len_one):
    print("Enter the element",i+1,"")
    element=input(":")
    if element.isdigit():
        List_one[i]=int(element)
check=input("Enter Y to enter index or N to skip it:")
if check.upper()=='Y':
    ind=int(input("Index value:"))
elif check.upper()=='N':
    ind=len_one-1
else:
    print("Invalid!")
a=my_pop(List_one,len_one,ind)
if a==1:
    print("Not executed!")
print("Removed value :",a)
print("Changed list: ",List_one,)
