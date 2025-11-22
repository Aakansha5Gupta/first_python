# write a program to check number is even or odd from this number to this number  using function 

def my_function():
    n1 = int(input("enter n1:"))
    n2 = int(input("enter n2:"))
    for n in range (n1,n2 +1):
        print (n)
        if n % 2 == 0:
            print("it is an even number")
        else:
                print("it is an odd number")
# this is my first call function 
my_function()
