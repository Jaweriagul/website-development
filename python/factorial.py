def factorial(n):
    if n==1:
      return n
    else:
       return n*factorial(n-1)
num = int(input("Enter a number"))
if num<0:
   print("sorry, the factorial of negative terms does not exist")
elif num==0:
   print("the factorial of 0 is 1")
else:
   print("the factorial of the number", num ,"is", factorial(num))      