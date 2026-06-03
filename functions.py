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

x = 100
def my_func():
    x = 50
    print(f"Inside : {x}")

my_func()
print(f"outside : {x}")

 