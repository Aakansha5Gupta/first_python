#string

str1 = 'Aakansha gupta'
str2 = "Aakansha gupta"
str3 = """Aakansha gupta"""

print(str1 + " " + str2)
print(len(str1 + str2 + str3)) #length

print(str1[0 :len (str1)]) #slicing

print(str1.endswith("ta")) #checking

print(str2.capitalize()) #capitalize

print(str3.replace("Aakansha" , "Goyal")) #Replacing

print(str1.find('k')) 

print(str2.count('a'))

#conditional Statment

a = int(input("First No "))
b = int(input("Second No "))

s = (input("Choose Simble "))

if(s == "*"):
    print(a*b)

elif(s == "+"):
    print(a+b)

elif(s == "-"):
    print(a-b)

elif(s == "/"):
    print(a/b)

elif(s == "%"):
    print((a/b)*100)

else:
    print("Unknown Simble")

mark =  int(input("Marks --> ",  )) 

if(mark >= 90):
    Mark = "A"
elif(mark >= 80 and mark < 90 ):
    mark = "B"
elif(mark >= 70 and mark <= 80):
    mark = "C"
elif(mark <= 69):
    mark = "D"

print(mark)
