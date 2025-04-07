#this file consists of topics related to python data type,numbers,Casting 
'''
Python built-in data types
Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
#You can get the data type of any object by using the type() function:

x=5
y='hello world'
z=7.0
print(type(x)) #<class 'int'>
print(type(y)) #<class 'str'>
print(type(z)) #<class 'float'>

#complex numbers in python (ie, the 3rd type of number data type)
'''
A complex number is a number that has:
A real part
An imaginary part that looks like this:
a=bj
where a=real part (like 2,3.5,-10,etc)
b=imaginary part
j=imaginary unit
following are eg using complex number
'''
#method 1:directly using a+bj

a=3+4j
print(a) #3+4j

#method 2:using complex() constructor

b=complex(3,4) # 3 is real,4 is imaginary
print(b) #3+4j

#accessing real and imaginary parts
#note:.real and .imag return float values

c= 3+4j
print(c.real) #3.0
print(c.imag) #4.0

#math operation with complex numbers
e=2+3j
f=1-4j
print(e+f) #(3-1j)
print(e-f) #(1+7j)
print(e*f) #(14-5j)
print(e/f) #(-0.5882352941176471+0.6470588235294118j)

'''
break down of calculation
for (a+b)
formula:(a+bj)+(c+dj)=(2+3j)+(1-4j)
(a+c)+(b+d)j=(2+1)+(3-4)j
ie; 3+(-1)j
ie;3-1j

for (a-b)
formula:(a + bj) - (c + dj) = (a - c) + (b - d)j
(2 + 3j) - (1 - 4j) = (2 - 1) + (3 - (-4))j = 1 + 7j

for(a*b)
formula:(a + bj)(c + dj) = (ac - bd) + (ad + bc)j
(2 + 3j)(1 - 4j)
= 2*1 + 2*(-4j) + 3j*1 + 3j*(-4j)
= 2 - 8j + 3j -12j²
= 2 - 5j -12(-1)
= 2 - 5j + 12
= 14 - 5j

'''
#Sequence Types:	list, tuple, range
#first let see list so list always listed in []
#Collection of items
g=["apple","banana","orange"]
print(type(g)) #<class 'list'>
print(g) #["apple","banana","orange"]

#second tuple so tuple uses ()

h=('cat','dog','birds')
print(type(h)) #<class 'tuple'>
print (h) #('cat','dog','birds')

# 3rd range so range is gonna give u a range from 0 to the value u give like x=range(6) so it will give range 0,6

i=range(11)
print(i) #range(0, 11)
print(type(i)) #<class 'range'>

#mapping type:dict it have a key value pair
#Key-value pairs write in{}

j={"name":"joy","age":"36"}
print(j) #{'name': 'joy', 'age': '36'}
print(type(j)) #<class 'dict'>

#set type:set and frozenset"
#set is writen in{} set = mutable = you can add/remove item

k={"apple","orange","banana"}
print(k) #{'banana', 'orange', 'apple'}
print(type(k)) #<class 'set'>

#frozenset  immutable = you cannot add/remove items after it's created

frozen=frozenset([1,2,3,4])
print(frozen) #frozenset({1, 2, 3, 4})

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a.union(b))         # frozenset({1, 2, 3, 4, 5})
print(a.intersection(b))  # frozenset({3})
print(a.difference(b))    # frozenset({1, 2})
print(b.difference(a)) #frozenset({4, 5})

#boolean type return true or false

l=True
print(l) #True
print(type(l)) #<class 'bool'>

#binary type:bytes ,bytearray,memoryview
#1) bytes:immutable binar data
'''
A sequence of bytes (like a string, but for raw data)
Immutable (can’t be changed once created)
'''
n=bytes([65,66,67]) #ASII:A=65,B=66,C=67
print (n) #n'ABC'
print(n[0]) #65

#2) bytearray:A mutable version of bytes
#You can change, append, or delete values

ba = bytearray([65, 66, 67])
ba[0] = 97   # Change A (65) to a (97)
print(ba)    # Output: bytearray(b'aBC')

ba.append(68)  # Add 'D'
print(ba)      # Output: bytearray(b'aBCD')

#memoryview-efficient data access
'''
A view (window) into binary data without copying it

Can wrap a bytes or bytearray object
'''
data = bytearray(b"hello")
view = memoryview(data)
print(view[0])   # Output: 104 (ASCII for 'h')

view[0] = 72     # Modify 'h' → 'H'
print(data)      # Output: bytearray(b'Hello')

#nonetype:No value
'''
Nothing

Empty

Null-like
'''
x = None
print(type(x))  # Output: <class 'NoneType'>
