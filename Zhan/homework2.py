A = "spam"
B = A
B = "shrubbery"
print(A)  #Result: Spam, NO

A = ["spam"]
B = A
B[0] = "shrubbery"
print(A) #Result: ["shrubbery"], YES

A = ["spam"]
B = A[:]
B[0] = "shrubbery"
print(A) #Result ["spam"], NO because we used range in 12 line

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  #Result: True, because they values are same
print(a is b)  #Result: False, because they reference(id) are not same

c = a
print(a is c) #Result: True because they reference(id) are same
#is checking are object same with their id == checking their values

print(id(a)) #Result: number of memory

#Object interning in Python is an optimization technique where Python reuses existing immutable objects with the same value instead of creating new ones.

a="Hello"
a=23    #Result: we don't need to delete first a for creating second a
#Garbage Collection (GC) in Python is an automatic memory management system that reclaims memory occupied by objects that are no longer in use by the program.