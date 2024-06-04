username = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()


x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 12
    
# func3()
# print(x)



def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual



f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))

# In Python, scopes determine the visibility and accessibility of variables, functions, and objects in different parts of your code. Scopes help organize and manage the names used in your program to avoid conflicts and provide a clear structure.

# There are four types of scopes in Python:

# Local Scope: Variables defined within a function are considered to be in the local scope. They are only accessible within that function. For example:
# In this example, the variable x is defined within the my_function() function, so it is only accessible within that function. If we try to access it outside the function, we'll get a NameError.

# Enclosing Scope: When a function is defined inside another function, the inner function has access to variables in the outer function's scope. This is called an enclosing scope. For example:
# In this example, the inner function inner_function() has access to the variable x defined in the outer function outer_function().

# Global Scope: Variables defined outside of any function or class have global scope. They can be accessed from anywhere in the code. For example:
# In this example, the variable x is defined outside of any function, so it has global scope and can be accessed from within the my_function() function.

# Built-in Scope: Python provides a set of built-in functions and objects that are always available in any Python program. These functions and objects are in the built-in scope. For example:
# In this example, the len() function is a built-in function that calculates the length of a string. It is available in the built-in scope and can be used directly without any import statements.

# Now, let's talk about closures. A closure is a function object that remembers values in the enclosing scope even if they are not present in memory. It allows a function to access and manipulate variables from an enclosing scope that has finished its execution. Here's an example:

# In this example, the outer_function() returns the inner_function() as a closure. The closure retains the value of x from the enclosing scope even after the outer_function() has finished executing. When we call the closure, it still has access to the value of x and prints it.

# Closures are useful when you want to create functions with pre-initialized values or when you want to create functions that can be customized with different parameters.

# I hope this explanation helps you understand scopes and closures in Python! Let me know if you have any further questions.
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
print(x)  # Error: NameError: name 'x' is not defined

# In this example, the variable x is defined within the my_function() function, so it is only accessible within that function. If we try to access it outside the function, we'll get a NameError.

# Enclosing Scope: When a function is defined inside another function, the inner function has access to variables in the outer function's scope. This is called an enclosing scope. For example:

def outer_function():
    x = 10  # Enclosing variable

    def inner_function():
        print(x)  # Accessing enclosing variable

    inner_function()

outer_function()  # Output: 10

# In this example, the inner function inner_function() has access to the variable x defined in the outer function outer_function().

# Global Scope: Variables defined outside of any function or class have global scope. They can be accessed from anywhere in the code. For example:

x = 10  # Global variable

def my_function():
    print(x)  # Accessing global variable

my_function()  # Output: 10

# In this example, the variable x is defined outside of any function, so it has global scope and can be accessed from within the my_function() function.

# Built-in Scope: Python provides a set of built-in functions and objects that are always available in any Python program. These functions and objects are in the built-in scope. For example:

print(len("Hello"))  # Output: 5

# In this example, the len() function is a built-in function that calculates the length of a string. It is available in the built-in scope and can be used directly without any import statements.

# Now, let's talk about closures. A closure is a function object that remembers values in the enclosing scope even if they are not present in memory. It allows a function to access and manipulate variables from an enclosing scope that has finished its execution. Here's an example:

def outer_function(x):
    def inner_function():
        print(x)  # Accessing variable from enclosing scope

    return inner_function

closure = outer_function(10)
closure()  # Output: 10