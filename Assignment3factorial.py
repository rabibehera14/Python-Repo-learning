n=int(input("enter a number"))
def factorial(n):
    if n<0:
        return "factorial is not possible for negative numbers"
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
print("Factorial of ",n ,"is" ,factorial(n))

