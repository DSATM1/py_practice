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