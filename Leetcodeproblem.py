print ("Construct Smallest Number From DI String");
print("You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.")
print("A 0-indexed string num of length n + 1 is created using the following conditions:num consists of the digits '1' to '9', where each digit is used at most once.")

import pandas as pd

#class InputNumber(str):
#    def inpt():
#        l=list(str)
#        print(l)


p1=("IIIDDDI")
n1=1
mylist=[]
mylist.append(n1)
#print(p1)
l=list(p1)
print(l)
for i in range(len(l)):
    print(i)
    if l[i] =="I":
        mylist.append(mylist[i-1]+1)
    if l[i]=='D':
        mylist.append(mylist[i-1]-1)

print(mylist);

