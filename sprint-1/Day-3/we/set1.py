# print("Hello World !")

# x=1
# print(type(x),x)

# y=float(3)
# print(type(y),y)

# z="abc"
# print( type(z),z)

# b=True
# print(type(b),b)

# list_values=[1,2,3,4]
# print(type(list_values),list_values)

# tuple_values=("a","b","c")
# print(type(tuple_values),tuple_values)

# dic={
#     "name":"ayush",
#     'place':"delhi"
# }

# print(type(dic),dic)


# sets={"a","b","c"}
# print(type(sets),sets)


# list_values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_values.append(20)
# print(list_values)
# list_values.remove(20)
# print(list_values)


# list_values=[1, 2, 3, 4]
# x=len(list_values)
# sum=0
# avg=0
# for i in range(x):
#     sum=sum+list_values[i]
# print(sum/x)


# def reverse(s):
#     str = ""
#     for i in s:        
#         str = i + str
#     return str
 
# s = "ayush"
# print(reverse(s))



# def count_vowels(s):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in s:
#         if char in vowels:
#             count=count+1
#     return count
# input_string=input("Enter a Input: ")
# num_vowels=count_vowels(input_string)
# print(num_vowels)



# def prime(num):
#     count=0
#     for i in range(1,num+1,1):        
#         if num%i==0:
#             count=count+1
   
#     if count==2:
#         print(num,"is a prime number")
#     else:
#         print(num,"is not the prime number")
# prime(13)


# def factorial(num):
#     mul=1
#     for i in range(1,num+1):
#        mul=mul*i
#     print(mul)
# factorial(5)



# def fibonacci_sequence(n):
#     sequence = []
#     if n >= 1:
#         sequence.append(0)  
#     if n >= 2:
#         sequence.append(1)  
#     for i in range(2, n):
#         sequence.append(sequence[i-1] + sequence[i-2])  #
#     return sequence


# num_terms = int(input("Enter the number of terms: "))
# fibonacci_seq = fibonacci_sequence(num_terms)
# print("Fibonacci sequence:", fibonacci_seq)



# num=10;
# list=[]
# for i in range(1,num+1):
#     list.append(i**2)
# print(list)


