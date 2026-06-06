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
    print("❌ Not Armstrong!")

print("Armstrong numbers from 1 to 1000:")

for i in range(1,1001):
    if amst(i):
        print(i,end= " ")"""
        

"""Enter num 1 : 45
Enter num 2 : 78
Enter num 3 : 33

Minimum : 33
Maximum : 78
Average : 52.00"""


"""def min_max(a,b,c): #type:ignore
    low = min(a,b,c) #type:ignore
    high = max(a,b,c)
    avg = (a+b+c)/3 #type:ignore
    return low, high, avg #type:ignore
res, res2, res3 = min_max(2,0,98)
print(f"Minium = {res}, Maximum = {res2}, Average = {round(res3,2)}")"""


"""def is_leap(year):

    if year % 400 == 0:
        return True
        #print(f"{year} is divisible by 400 → ✅ Leap Year!")
    elif year %100 == 0:
        return False 
        #print(f"{year} is divisible by 100 but not 400 → ❌ Not a Leap Year!")
    elif year % 4 == 0:
        return True 
        #print(f"{year} is divisible by 4 but not 100 → ✅ Leap Year!")
    else:
        return False    
        #print("❌ Not a Leap Year!")
year = int(input("Enter a year :").strip())
print(is_leap(year))

print("Leap years from 2000 to 2100:")
for i in range(2000, 2101):
    if is_leap(i):
        print(i,end=" ")"""

"""Enter n : 8
Series  : [0, 1, 1, 2, 3, 5, 8, 13]
Sum     : 33
Average : 4.13"""

"""def fibonacci(n):
    series = []
    a = 0
    b = 1

    for i in range(n):
        series.append(a)
        a,b = b,a+b
    return series
n = int(input("Enter n :").strip())
series = fibonacci(n)
total = sum(series)
avg = total / len(series)
print(f"Series : {series}")
print(f"Sum : {total}")
print(f"Average : {avg}")"""


#print("\n===== Mini Bank =====")


"""def display_menu():
    print("\n===== Mini Bank =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def check_balance(balance):
    print(f"Current Balance : ₹{balance:.2f}")
    return balance


def deposit(balance):
    amount = float(input("Enter deposit amount: ").strip())

    if amount <= 0:
        print("Enter a positive amount.")
    else:
        balance = balance + amount
        print(f"Deposited ₹{amount:.2f}")
        print(f"New Balance : ₹{balance:.2f}")

    return balance


def withdraw(balance):
    amount = float(input("Enter withdrawal amount: ").strip())

    if amount <= 0:
        print("Enter a positive amount.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance = balance - amount
        print(f"Withdrawn ₹{amount:.2f}")
        print(f"New Balance : ₹{balance:.2f}")

    return balance


def main():
    balance = 10000.00

    while True:
        display_menu()

        choice = input("Choose option: ").strip()

        if choice == "1":
            balance = check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


main()"""


# print("\n--- Result Card ---")


"""def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 35:
        return "E"
    else:
        return "F"

def result_card(s1, s2, s3, s4, s5):
    subjects = [s1, s2, s3, s4, s5]

    total = 0
    failed = False

    for mark in subjects:
        total = total + mark

        if mark < 35:
            failed = True

    percentage = (total / 500) * 100
    grade = get_grade(percentage)

    if failed:
        result = "FAIL"
    else: 
        result = "PASS"

    print("\n--- Result Card ---")
    print(f"Total      : {total}/500")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Result     : {result}")


result_card(96, 23, 90, 85, 85)"""

"""get_grade(86.6) → "A"
--- Result Card ---
Total      : 433/500
Percentage : 86.60%
Grade      : A
Result     : ✅ PASS"""


"""Concise step-by-step approach and logic-building tips for both programs:

Mini Bank

 1. Understand requirements: menu loop, separate functions, keep running until exit.
 2. Break into functions: display_menu(), check_balance(balance), deposit(balance), withdraw(balance), main().
 3. Define inputs/outputs: functions take/return balance; main holds state.
 4. Validate inputs: numeric, positive, sufficient funds for withdraw.
 5. Format output (currency) and print confirmations.
 6. Test with sequences (depositâwithdrawâexit) and edge cases (invalid input, overdraft).

Marks Program

 1. Understand: compute total, percentage, grade, pass/fail.
 2. Break into functions: get_grade(percentage) and result_card(s1..s5).
 3. result_card: sum subjects â total, percentage = total/500*100, check any mark<35 â FAIL.
 4. Call get_grade(percentage) to get grade string.
 5. Print formatted result card; test boundary grades and failing marks.

General logic-building skills    

 - Decompose: split tasks into single-responsibility functions.
 - Start simple: get a working path, then add validation and formatting.
 - Think in data flow: what each function receives and returns.
 - Handle edge cases early (invalid input, boundaries).
 - Iterate and test small units; add print/debug statements.
 - Read other solutions and refactor for clarity and reuse."""
