'''a = 12
print(a)
print(type(a))

b = 12.23
print(b)
print(type(b))

c="Durgesh"
print(c)
print(type(c))

d = 23+ 34j
print(d)
print(type(d))

n = int(input("Tell me data type"))

print(type(n))

print("Two points are S and R")

print("The coordinate of S are x1 and y1:")
print("The coordinate of R are x2 and y2:")

x1 = int(input("Enter value of x1:"))
y1 = int(input("Enter value of y1:"))
x2 = int(input("Enter value of x2:"))
y2 = int(input("Enter value of y2:"))


distance = ((x1 -x2)**2+(y1-y2)**2)**.5
formatted_string=(f"{distance:.2f}")
print(formatted_string)


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

a, b = b, a
print("After swapping:")
print("a =",a)
print("b =",b)



    
n =int(input("Enter the number: "))
for num in range(1,n+1):
    sum=0

    for i in range(1,num):
           if num%i==0:
               sum +=i
    if sum ==num:
          print(num,"number is perfect")


n=int(input("enter the table number:"))
for i in range(1,11):
         print(n, "x",i,"=",n*i, )



#line by line table
for i in range(1,11):
    for n in range(2,10):
        print(f"{n} x {i} ={n*i}".ljust(12),end=" ")
    print()


#reverse number
n=int(input("Enter positive number:"))
rev=0
while n>0:
    
   num =n%10
   rev =rev*10+num
   n=n//10

print("reversed number:",rev)'''




   
   
   


      
      





