# Problem 1: Print the following pattern
# num=5
# for i in range(1,num+1):
#     bag=""
#     for j in range(i):
#         bag=bag+str(j)+" "
#     print(bag)

# Problem 2: Display numbers from a list using loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# x=len(numbers)
# for i in range(x):
#     if numbers[i]<=150 and numbers[i]%5==0 and numbers[i]<500:
#         print(numbers[i])    
#     elif numbers[i]>500:
#         break;
    

### Problem **3: Append new string in the middle of a given string**

# s1="Ault"
# s2="Kelly"
# def append(s1, s2):
#     middle_index = len(s1) // 2
#     s3 = s1[:middle_index] + s2 + s1[middle_index:]
#     return s3

# result=append(s1,s2)
# print(result)


# Problem 4: Arrange string characters such that lowercase letters should come first

# str1 = "PyNaTive"
# x=len(str1)
# Lower=""
# upper=""
# for i in range(x):
#     if str1[i]==str1[i].lower():
#         Lower+=str1[i]
#     else:
#         upper+=str1[i]
# print(Lower+upper)


# Problem 5: Concatenate two lists index-wise

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# x=len(list1)
# y=len(list2)
# z=min(x,y)

# list3=[]

# for i in range(z):
#     a=list1[i]+list2[i]
#     list3.append(a)
# print(list3)


# Problem 6: Concatenate two lists in the following order

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# x=len(list1)
# y=len(list2)
# z=min(x,y)

# list3=[]

# for i in range(x):
#     for j in range(y):
#         a=list1[i]+list2[j]
#         list3.append(a)
# print(list3)


# Problem 7: Iterate both lists simultaneously

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# x=len(list1)
# y=len(list2)
# for i in range(x):
#     bag=""
#     for j in range(y-1,-1,-1):
#         print(list1[i],list2[j])
#     break   
    

# Problem 8: Initialize dictionary with default values

# def assign_defaults(employees, defaults):
#     employee_defaults = {}
#     for employee in employees:
#         employee_defaults[employee] = defaults
#     return employee_defaults


# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# output = assign_defaults(employees, defaults)
# print(output)


# Problem 9: Create a dictionary by extracting the keys from a given dictionary


# def sample(sample_dict,keys):
#     emp={}
#     for i in keys:
#         emp[i]=sample_dict["name"]
#     return emp

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# print(sample(sample_dict,keys))


# Problem 10: Modify the tuple

# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0]=222
# print(tuple1)



    

       