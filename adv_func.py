# def outer():
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#         inner()
# outer()    

# def welcome(name):
#     print(f"Welcome {name}!")
# a = welcome
# print(f"Welcome: {welcome}")
# print(f"a: {a}")
# a("Shyam")


# def increment(num):
#     def increase_by(factor):
#         return num + factor
#     #value= increase_by(10) 
#     return increase_by
# increase_by=increment(20)
# print(increase_by(20))
# print(increase_by(10))

# def welcome(name):
#     print(f"Welcome {name}")

# def bye_bye(name):
#     print(f"Bye bye {name}") 
    
# def greet_ram(a):
#     a("Ram")
# greet_ram(welcome)

def decorate_function(func):
    def wrapper():
        print("called before.")
        func()
        print("called after.")
    return wrapper

@decorate_function 
def example():
    print("I am example.")

example()

           