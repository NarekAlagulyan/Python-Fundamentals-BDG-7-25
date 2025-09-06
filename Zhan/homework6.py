# print((1, 2, 3) * 2) #Result: (1, 2, 3, 1, 2, 3)
# print((1) == 1) #Result: True
# t = ("a", "b", "c")
# (a, b, c) = t
# print(a)
# print(b)
# print(c)
# cords=(input("x:"),input("y:"))
# x,y=cords
# print(x,y)
# countOfStudents=int(input("how many students we have"))
# listOfStudents=[]
# for i in range(countOfStudents):
#     listOfStudents.append((input("Student Name:"),input("Student Score:")))
# # print(listOfStudents)
# with open("greeting.txt","w") as file:
#     file.write(f"Hello {input('Name:')}")
# with open("greeting.txt","r") as file:
#     print(file.read())
# with open("greeting.txt","w") as file:
#     file.write(f"Hello {input('Name:')}\n"*3)
# with open("greeting.txt","r") as file:
#     lines = file.readlines()
#     for line in lines:
#         line = line.replace("\n",'')
#         print(line)
import random
from _datetime import datetime
#
# with open("mylog.txt", 'w') as f:
#     f.write(input("Write something: ")+" "+str(datetime.now()))
# with open("greeting.txt", 'w') as f:
#     with open("mylog.txt", 'r') as g:
#         f.write(g.read())
# with open("greeting.txt",'a')as file:
#     file.write(str(datetime.now()))
#
# with open("greeting.txt",'w')as file:
#     for i in range(10):
#         file.write(str(random.randint(1,10)))
#         file.write("\n")
# with open("greeting.txt",'r')as file:
#     sum=0
#     for line in file:
#         sum=sum+int(line)
# print(sum)

# myList = []
# a=True
# i=0
# while a:
#     i+=1
#     sentence=input(f"Please write line {i} (if you want to end Please write False)")
#     if sentence=="False":
#         a=False
#     else:
#         myList.append(sentence.split())
#
# with open("greeting.txt",'w')as file:
#     for i in myList:
#         for j in i:
#             file.write(j+", ")
#         file.write("\n")








