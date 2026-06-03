#print("Welcome to functions")
# print("Hello Suraj! Welcome.")
# print("Hello Putta! Welcome.")
# print("Hello Ravi! Welcome.")

"""def greet(name): #type:ignore
    print(f"Hello {name}, Good Eve!")

greet("Suraj")
greet("Putta")"""

"""def add(a,b): #type:ignore
    print(a+b) #type:ignore

result = add(5,3)
print(result)"""

"""def add_return(x,y): #type:ignore
    return x+y  #type:ignore
result = add_return(10,20)
print(result)
print(result*2)"""

"""def stu_info(name, age, cgpa): #type:ignore
    print(f"Suraj : {name}| Age : {age} | CGPA : {cgpa}")

stu_info("Suraj",24,8.5)  # right order
stu_info(8.5,"Suraj",1)  # wrong order"""

"""x = 100
def my_func():
    x = 50
    print(f"Inside : {x}")

my_func()
print(f"outside : {x}")"""

 
"""a = 100

def in_side():
    a = 50
    print("inside",a)

in_side()
print("outside",a)"""

"""def hello(name="Suraj",message="Ai Engineer"):   #type:ignore
    print(f"Hello {name} in next few months u r becoming {message}")

hello()
hello("Putta","Collegue of Mr. Suraj S P")"""

"""def min_max(a,b,c,d): #type:ignore
    low = min(a,b,c,d) #type:ignore
    high = max(a,b,c,d) #type:ignore
    return low, high #type:ignore
res, res2 = min_max(2,0,98,9)
print(f"Minium = {res}, Maximum = {res2}")"""

"""# Example: Fibonacci sequence generator (commented)
# This function returns a list containing the first n Fibonacci numbers.
# It demonstrates iteration, tuple unpacking, and returning a collection.
def fibonacci(n):  # type:ignore
    """Return a list with the first n Fibonacci numbers."""
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Demonstration / usage example:
print("Fibonacci(7):", fibonacci(7))  # expected: [0, 1, 1, 2, 3, 5, 8]
"""