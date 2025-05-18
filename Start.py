# a = 10
# b = 5.5
# c = "python"
#
# print("sum:", a+b)
# print("Type of c:",type(c))
#
# x = int(input("Enter a number:"))
#
# if x > 0:
#     print("Positive Number")
# elif x == 0:
#     print("zero")
# else:
#     print("Negative Number")
from importlib.resources import contents

# char = input("enter a character")[0]
# print("your entered :",char)
#
# if len(char) == 1:
#     print("valid")
# else:
#     print("enter only one character")


# fruits = [ "apple","banana","mango"]
# for i in fruits:
#     print("i likes",i)
#
# for i in range(1,101):
#     print(i)

# j=1
# while j<=5:
#     print("while loop j:",j)
#     j=j+1

#
# def great(name):
#     print("Hello",name)
#
# great("kishore")
# great(1)

# def sum_uoto(n):
#     if n==0:
#         return 0
#     return n+sum_uoto(n-1)
#
# print(sum_uoto(5))

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
#
# x = factorial(5)
# print(x)


# my_list = [1,2,3,"kishore",True]
# print(my_list[0])
# my_list.append(10)
# my_list.remove(2)
# print(my_list)
#
#
# my_tuple = (3,2,3,4)
# print(my_tuple)
#
# my_set = {1,5,8,0,1,4,5,6,7}
# print(my_set)
#
# my_dict ={"name":"kishore","age":21}
# print(my_dict)
# my_dict["location"] = "India"
# print(my_dict)
#
#
# nums =[1,2,3]
# nums.append(4)
# print(nums)
#
# t = (10,20,30)
# print("Tuple:",t)
#
# s = {1,2,3,3}
# print("set s:",s)
#
# student = {"name":"kishore","course":"python"}
# student["progress"] = "Excellent"
# print("Dict:",student)

# squares = [x*x for x in range(1,6)]
# print(squares)
#
# unique_lengths = {len(word) for word in ["apple","banana","kiwi"]}
# print(unique_lengths)
#
# nums = [1,2,3]
# squares ={x:x*x for x in nums}
# print(squares)

# try:
#     num = int(input("enter a number: "))
#     result =10/num
#     print("result:",result)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("please enter a valid number")
# finally:
#     print("Done!")


# with open("demo.txt","w") as file:
#     file.write("Hello, Kishore!\n")
#     file.write("This is your first file.\n")
#
# with open("demo.txt","r")as file:
#     content = file.read()
#     print("File content:\n",content)





