#Create a list and print all elements using a loop
#Add an element to the list
#Remove an element from the list
#Find the maximum number in a list
#Find the length of the list
l=[10,20,35,85,70,26]
for i in l:
  print(i)
l.append(54)
print(l)
l.remove(35)
# print(l)
# print(max(l))
# print(len(l))
     a=[0,1,0,1,1,1,1,1,0]
i=0
pos=0
while(i<len(a)):
    if(a[i]==0):
        a[i],a[pos]=a[pos],a[i]
        pos+=1
    i+=1
print(a)



# 1. Create a list and print all elements using a loop
numbers = [10, 25, 5, 40, 15]

print("Original list elements:")
for num in numbers:
    print(num)

# 2. Add an element to the list
numbers.append(50)
print("\nAfter adding 50:", numbers)

# 3. Remove an element from the list
numbers.remove(5)
print("After removing 5:", numbers)

# 4. Find the maximum number in a list
max_number = max(numbers)
print("Maximum number:", max_number)

# 5. Find the length of the list
list_length = len(numbers)
print("Length of the list:", list_length)
