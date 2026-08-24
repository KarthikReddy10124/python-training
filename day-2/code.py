## Age form
##nested if else condition


# age = float(input("Enter your age"))

# if(age<18):
#     print("Under age")
# elif(age>=18 and age<=45):
#     print("Mid Age")
# elif(age>=45 and age<=50):
#     print("Senior mid age")
# else:
#     print("Senior Citizen56")



# nested ifelse

# age = float(input("Enter the age"))
# if (age<18):
#     print("Minor age")
#     if (age<15):
#         print("You are in school")
#     else:
#         print("you are in clg")
# elif(age>=18 and age<=45):
#     print("Mid Age")
# elif(age>=45 and age<=50):
#     print("Senior mid age")
# else:
#     print("Senior Citizen56")



## Loops statement
## for loop, while loop

# lst=[1,2,3,4,5,6,7,8,9,10]
# for i in lst:
#     print(i**2)



##find the sum of all the elements in the list

# lst=[1,2,3,4,5,6,7,8,9,10]
# sum1=0
# for i in lst:
#     sum1=sum1+i
# print(sum1) 



## find the sum of even and odd number

# lst = [1,2,3,4,5,6,7,8,9,10]
# even_sum = 0
# odd_sum = 0

# for i in lst:
#     if (i%2==0):
#         even_sum=even_sum+i
#     else:
#         odd_sum=odd_sum+i
# print("Even sum is {}".format(even_sum))
# print("Odd sum is {}".format(odd_sum))



## while condition
# lst=[1,2,3,4,5,6,7]

# i=0
# even_sum=0
# odd_sum=0
# while(i<=10):
#     if(i%2==0):
#         even_sum=even_sum+i
#     else:
#         odd_sum=odd_sum+i

#     i=i+1
# print(even_sum,odd_sum)



##break

# x=1
# while(x<7):
#     print(x)
#     if x==4:
#         break
#     x=x+1



## continue

x=1
while(x<7):
    x=x+1

    
    if x==4:
        continue
    print(x)