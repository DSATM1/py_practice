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

"""n = int(input("Enter the number:").strip())
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz",end = " ")
    elif i % 3 == 0:
        print("Fizz",end = " ")
    elif i % 5 == 0:
        print("Buzz", end = " ")
    else:
        print(i,end= " ")  """


"""Enter number : 12345
Sum of digits : 15

Enter number : 9999
Sum of digits : 36



n = int(input("Enter the number:").strip())
new_rev = 0
while n > 0:
    last_digit = n % 10
    new_rev = new_rev * 10 + last_digit
    n = n // 10    
print(f"Reverse : {new_rev}")

```
Enter the number: 12345

```


```
Reverse : 54321
```"""

"""n = int(input("Enter the number:").strip())

count = 0
while n > 0:
    last_digit = n % 10
    count = count + last_digit
    n = n//10
print(f"Sum of Digits: {count}")"""

"""Fibonachii Series"""

"""n = int(input("Enter the number:").strip())
a = 0
b = 1
for i in range(n):
    print(a,end =" ")
    a,b=b,a+b"""

"""
A number is Armstrong if sum of its digits raised to power of number of 
digits equals the number itself. Check if given number is Armstrong.

Enter number : 153
153 = 1³ + 5³ + 3³ = 153 ✅ Armstrong Number!

Enter number : 123
123 ❌ Not an Armstrong Number!


n = int(input("Enter number:").strip())
count = 0
if n==0:
    count += 1
while n > 0:
        n = n // 10
        count += 1
print(f"Number of digits : {count}")

"""

"""n = int(input("Enter the number:").strip())

count = 0 
if n == 0: 
    count +=1
    while n > 0:
        last_digit = n % 10
        count+=last_digit**3
        n = n//10
if n == n**3:
    print(f"{count} ✅ Armstrong Number!")
else:
    print(f"{count} ❌ Not an Armstrong Number!")"""


"""n = int(input("Enter the number: ").strip())
original = n         # save n before touching it!

# Step 1: count digits
temp = n
power = 0
while temp > 0:
    temp = temp // 10
    power += 1

# Step 2: extract digits and compute armstrong sum
temp = n                # reset temp to n again!
armstrong_sum = 0
while temp > 0:
    last_digit = temp % 10
    armstrong_sum += last_digit**power  # digit ** power
    temp = temp // 10

# Step 3: compare
if original == armstrong_sum:
    print("✅ Armstrong!")
else:
    print("❌ Not Armstrong!")"""



"""
Take N as input. Print all prime numbers from 2 to N using nested loops.

Enter N : 30
2 3 5 7 11 13 17 19 23 29"""



"""n = int(input("Enter n:").strip())
is_prime = True #we assuming 
for num in range(2, n+1):
    is_prime = True    #← reset every iteration!
        
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
       print(num)"""

