def pow(n1,n2):
    return n1 + n2

def run(func,num1,num2):
    print(func(num1,num2))

run(pow,2,5)


def say_hello(name):
    return f"hello {name}"

def be_awesome(name):
    return f"yo {name} , together we are the awesomest"

def greet_bob(func):
    return func("Bob")



print(greet_bob(say_hello))

print(greet_bob(be_awesome))

def perent():
    print("peremt()")

    def first_child():
        print("first_child")

    def second_child():
        print("second_child")

    print(second_child())
    print(first_child())

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

print(parent())


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

# first = parent(1)
# second = parent(2)
print(parent(1)())
print(parent(2)())

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

# sey = my_decorator(say_whee)()
print(say_whee( ))

def outer_func():
    var = 100

    def inner_func():
        print(f"Printing var from inner_func(): {var}")
        print(f"Printing another_var from inner_func(): {another_var}")

    another_var = 200  # This is defined after calling inner_func()
    inner_func()gb
    print(f"Printing var from outer_func(): {var}")


outer_func()

def plus_one(number):
    return number + 1

def func(func):
    num = 5
    return func(num)

print(func(plus_one))



def uppercase_decarator(func):
    print(f"{func()}".upper())

#@uppercase_decarator
def say_hi():
    return 'hello there'

say = uppercase_decarator(say_hi)

print(say_hi)







