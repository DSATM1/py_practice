#print("Practicing Functions ")



"""def is_even(n): #type:ignore
    if n % 2 == 0:
        return True
    else:
        return False    
res = is_even(1)
print(res)"""
''
"""def is_even(n):  #type:ignore
    return n % 2 == 0  #type:ignore
n = int(input("Enter n:").strip())
result = is_even(n)
if result == True :
    print(f" {n} is Even ✅")
else:
    print(f"{n} is Odd ❌")"""


"""def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact 

n = int(input("Enter n:").strip())
fact = factorial(n)
print(f"{n}! : {fact}")"""



"""cel=int(input("Enter Temp in Celcius :"))
print(f"Fahrenheit : {(cel*9/5)+32} F")
print(f"Kelvin : {(cel+273.15)} K")"""

"""def cel(temp):
    cel = ((temp*9/5)+32)
    kel = temp+273.15
    return cel,kel  
temp=int(input("Enter Temp in Celcius :"))
res = cel(temp)
print(res)"""


"""def celsius_to_fahrenheit(c):   # one parameter only!
    cel = ((c*9/5)+32)
    k = c+273.15
    return cel,k
res = float(input("Enter Temp in Celcius :"))
faren, kelvin = celsius_to_fahrenheit(res)
print(f"Fahrenheit : {faren} F")
print(f"kelvin : {kelvin} K")"""

"""def calculator(a,b,op):
    if op =="+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b == 0 : 
            return "Error: Division by zero"
        else :
            return a/b 
    else:
        print("Invalid Operator")
a = float(input("Enter a :").strip())
b = float(input("Enter b :").strip()) 
op = input("Enter Operator:").strip()       
res = calculator(a,b,op)
print(res)"""


"""def is_palindrome(str):
    l = len(str)
    #left = 0
    #right = 0 
    
    for i in range(0,l//2):
        #left = i
        #right = l - i - 1 
        if str[i] != str[l - i - 1]:
            return False
    return True 

str = input("Enter a String:").strip().lower()
print(is_palindrome(str))"""

"""
def power(base, mele):
    result = 1
    # if mele == 0:
    #     return 1
    for i in range(0,mele):
        result= result * base
    return result
res = power(2,10)
print(res)"""


"""def greet(name,message="Morning !"):
    if message == "Morning !":
        print(f"Morning 🌅, {name}")
    elif message == "Night":
        print(f"Night 🌙, {name}")
    elif message == "Afternoon":
        print(f"Afternoon ☀️, {name}")
    else:
        print(f"Evening 🌆, {name}")
    
greet("Suraj")
greet("Suraj", "Night")
greet("Suraj", "Afternoon") 
greet("Suraj", "Evening") """


#count of vowels
# aeiouAEIOU
#for loop 


"""def count_vowel(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count = count+1
    return count
res = input("Enter a string :").strip()
print(count_vowel(res))"""



# is_armstrong(153) → True
# is_armstrong(123) → False

# Armstrong numbers from 1 to 1000:
# 1 2 3 4 5 6 7 8 9 153 370 371 407

# n = int(input("Enter the number: ").strip())
# original = n

# power = len(str(n))   # count digits directly

# armstrong_sum = 0

# while n > 0:
#     digit = n % 10
#     armstrong_sum += digit ** power
#     n = n // 10

# if original == armstrong_sum:
#     print("✅ Armstrong!")
# else:
#     print("❌ Not Armstrong!")

"""def amst(n):
    original = n

    power = len(str(n))   # count digits directly

    armstrong_sum = 0

    while n > 0:
        digit = n % 10
        armstrong_sum += digit ** power
        n = n // 10

    return original == armstrong_sum
  
n = int(input("Enter the number: ").strip())

if amst(n):
    print("✅ Armstrong!")
else:
    print("❌ Not Armstrong!")"""