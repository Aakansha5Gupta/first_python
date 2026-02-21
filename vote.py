 x=int(input("enter your age:"))
y=input("you have ticket(yes/no):")
if x>=18 and y=="yes" :
    print("you are eligible")
else:  
    print("you are not eligible")  
###############################################
x=int(input("enter your age:"))
y=input("you have ticket(yes/no):")
if x>=18 :
    if y=="yes" :
        print("yoy are eligible")
    else :
        print("you have not ticket")    
else:  
    print("you are not eligible")  
###############################################
for i in range(5):
    print (i)
 ###################################################
x=int(input("en(ter a number:"))
for i in range (6,x,2):
    print(i)  
#########################################################

x=int(input("enter number:"))
k=1
for i in range (1,x+1,1):
  k=k*i

  print(k)
