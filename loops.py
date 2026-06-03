"""n = int(input("Enter n:").strip())
is_prime = True #we assuming 
if n<=1: #if any user enter 0 or 1 
    is_prime = False # then it's not a prime
else:
    for i in range(2, n): #n or n-1 both can use 
        if n % i == 0: # n = 17 and i start from 2 so n=17 and i=2 until i = 16 no divisor found 
            is_prime = False # so this executes 
            break   # and braks the loop 
if is_prime: # proving 
    print(f"{n} is a Prime number ✅")
else:
    print(f"{n} is NOT a Prime number ❌")"""

"""class Solution:
    def rev(self,x):
        # i = 0
        # while x = i*x:
        #     print("NA")
        # if 
        for i in range(1,11,-1):
            print(f"{x} = {i} x {i*x} ")
if __name__ == "__main__":
    if rev(x):"""
#if x = 3 then ans = 3 2 1 0;

"""Divisible by both 3 and 5  →  print "FizzBuzz"
Divisible by 3 only        →  print "Fizz"
Divisible by 5 only        →  print "Buzz"
Otherwise                  →  print the number"""

n = int(input("Enter the number:").strip())
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz",end = " ")
    elif i % 3 == 0:
        print("Fizz",end = " ")
    elif i % 5 == 0:
        print("Buzz", end = " ")
    else:
        print(i,end= " ")  
