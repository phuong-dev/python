'''
Created on Nov 13, 2019

@author: phuong
'''
'''
1.
Co the gan nhieu loai gia tri ( so , chuoi ) cho mot bien
Tuy nhien khi in ra cau lenh se lay gia tri ( so , chuoi ) cuoi cung ma ban nhap cho bien
'''
hg = 1
hg = "Hello World"
hg = [ 1, 2, 3]
hg = [1.2 , "Hello" , "W" , 2]
print(hg)

'''
2.Toan tu logic
'''
xa = 1
if not xa > 1:
    print("not returned True")
else:
    print("not returned False")
    
'''
'''
    
fruits = ["banana" , "apple" , "mango"]
for fruit in fruits:
    print("Current fruit : " , fruit)

print("Good bye!")


count  = 0
while ( count < 9 ):
    count = count + 1
    print("The count is : " , count)
    break
 
 
a = 1
b = 2
def sum(a , b):
    return( a + b )
print("the total of a and b is: " , sum(a, b))

c = 2 
d = 3
def total(c , d):
    return( c + d )
print("the total of c and d is: " , total(c, d))


def plus(e,f = 10):
    return ( e + f)
print("plus of e and f is : " , plus(2))


str1 = "Hello"
str2 = "World"
str3 = "123123123123sdfsdfsdfsdf"
print(str1[0])
print(str2[0]
      , str2[1]
      , str2[2]
      , str2[3]
      , str2[4]
       )
str = str1 + " " + str2
print(str)
print(str[0:7])
print(str1[-3:])
print("the length of str3 is: ",len(str3))
newstr = str1.replace("Hel", "a")
print(newstr)


car = "Mazda"
length = len(car[-1])
last = car[length]
print(last)



index = 0
while index < len(car):
    letter = car[index]
    print(letter)
    index = index + 1


animal = 0
farm = "barns"
while animal < len(farm):
    countAnimal = farm[animal]
    print(countAnimal)
    animal = animal + 1

str12 = 1
str13 = "123123"
print(str13.find("2"))


numbers123 = [ 1, 2 , 3 , 4]
del numbers123[0:2]
print(numbers123)

str2 = "How long does it take?"
print(str2.split(" "))


s123 = "test string"
print(f"String = \"{s123}\" ")