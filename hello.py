def factorial(n):
  if n==0:
     result=n*factorial(n-1)
     return result
     
n=int(input("enter the number"))
print(factorial(n))
