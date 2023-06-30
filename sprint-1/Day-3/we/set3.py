# Question 1

# list_val= [("John", 25), ("Jane", 30)]
# x=len(list_val)
# for i in range(x): 
#     char=""  
#     for j in range(x):
#         char=list_val[i][j]
#         print(char)

# Question 3

# list_values=[2,15,11,7]
# target=9
# x=len(list_values)
# output=[]
# for i in range(x-1):
#     for j in range(x):
#        sum=list_values[i]+list_values[j]
#     if sum==target:
#         output.append(i)
#         output.append(j)
       
   
# print(output)

#Question 4  
# string = input("Enter Your Input: ")
# strlength = len(string)
# bag = ""
# for i in range(strlength-1, -1, -1):
#    bag = bag + string[i]

# if string==bag:
#    print(f"The word {string} is a palindrome")
   
# Question 5
# def selection_sort(arr):
#     n = len(arr)
    
#     for i in range(n-1):
#         min_idx = i
        
 
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
        
        
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
#     return arr


# arr = [64, 25, 12, 22, 11]
# sorted_arr = selection_sort(arr)
# print("Sorted array:", sorted_arr)

    
# Question 7
# bag=""
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         bag=bag+"Fizz Buzz"+" "
#     elif i%5==0:
#         bag=bag+"Buzz"+" "
#     elif i%3==0:
#         bag=bag+"Fizz"+" "
#     else:
#         bag=bag+str(i)+" "
# print(bag)

# Question 8

# file = open("input.txt", "r")
# text = file.read()
# file.close()
# list_value=[]
# list_value.append(text)
# print(list_value)

# file=open("output.txt","w")
# text=file.write("Number of word:{}")
# print(len(text))


# Question 9
# first_input=int(input("Enter Your first Input :"))
# second_input=int(input("Enter Your second Input :"))

# def exception(first_input,second_input):
#     if second_input==0:
#         print("Cannot divide by zero")
#     else:
#         x=first_input//second_input
#         print(x)

# exception(first_input,second_input) 