'''a=[1,2,3,4,1,2,3,12,3,33,]
s=set(a)
print(s)
if 4 in s:
    print("Element is present")
else:
    print("Not prsesnt in list")'''
'''a=['b','c','d','e','a','s','d','a','s']
s=set(a)
print(s)'''
'''for i in range(2,10,2):
    print(i)
for i in range(1,11):
    print(i,end=" ")'''
'''i=1
while i<=2:
      print(i)'''
'''a=[1,2,1,2,1,3,2,4,3,2,3]
s=len(a)
target=1
count=0
for i in range(s):
    if a[i]==target:
        count+=1
    print(count)'''
'''a=[1,2,1,2,1,3,2,4,3,2,3]
d={}
for i in a:
    if i in d :
        d[i]+=1
    else:
        d[i]=1
    print(d)'''
a=[1,2,1,2,1,3,2,73,4,3,2,3]
maxi=a[0]
for i in a:
    if i>maxi:
        maxi=i
print(maxi)




 