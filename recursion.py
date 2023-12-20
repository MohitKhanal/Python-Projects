r1=int(input("Enter the number you want to find factorial upto:"))
for i in range(1,r1+1):
    def factorial(n):
        if n==1 or n==0:
            return 1
        else:
            return n*factorial(n-1)
    print(factorial(i))




