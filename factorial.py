n=int(input("Enter a number:"))
f=1
if n>0:
     for i in range(1,n+1):
         f=f*i
     print("Factorial of", n, "=", f)

