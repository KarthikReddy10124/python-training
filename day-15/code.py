# #Create a list and print all elements using a loop
# #Add an element to the list
# #Remove an element from the list
# #Find the maximum number in a list
# #Find the length of the list
# l=[10,20,35,85,70,26]
# for i in l:
#   print(i)
# l.append(54)
# print(l)
# l.remove(35)
# # print(l)
# # print(max(l))
# # print(len(l))
#      a=[0,1,0,1,1,1,1,1,0]
# i=0
# pos=0
# while(i<len(a)):
#     if(a[i]==0):
#         a[i],a[pos]=a[pos],a[i]
#         pos+=1
#     i+=1
# print(a)

a=[1,2,4,2,4,6,2,5,4]
i=0
maxx=0
while(i<len(a)):
    j=i
    le=1
    while(j+1<len(a)):
        if(a[j]<a[j+1]):
            le+=1
        else:
            if(le>maxx):
                maxx=le
            break
        j+=1
    i+=1
print(maxx)

#sliding window technique
a=[1,2,4,2,4,5,7,8,9,10,2,3,2,2,2,4,5]
i=0
j=0
maxx=0
count=0
while(j+1<len(a) and i<=j):
    if(a[j]<a[j+1]):
        count+=1
        j+=1
    else:
        if(count>maxx):
            maxx=count
        count=1
        i=j+1
        j=i
print(maxx)
        
    
    
        