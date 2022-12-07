
# def sum():
#     a=int(input("enter first number:"))
#     b=int(input("enter second number:"))
#     c=int(input("enter third number:"))
#     s=a+b+c
#     print("Addition of three number",s)
#     return s
# print(sum()) 

# def profile(name,address,contact):
#     print(f"Name: {name}")
#     print(f"Address: {address}")
#     print(f"Contact: {contact}")

# profile("Ram", "Ktm","987654321") #->positional Argument
# print("------------------------")
# profile("Ram", "987654321","Ktm")
# print("------------------------")
# print("------------------------")
# profile(name="Ram",address="Ktm",contact="987654321") #->keyword Argument
# print("------------------------")
# profile(name="Ram",contact="987654321",address="Ktm")


#*args,**kwargs

def examples(*args):
    print(args)
examples(1,2,3,4,5) 


def example2(**kwargs):
    print(kwargs)  
example2(name="Ram",contact="987654321",nickname="Ra")    

def mix_function(*args,**kwargs):
    print(args)
    print(kwargs)
mix_function(1,2,3,name="Ram",nickname="Ra") 

def multiple_of_number(num1,factor=5):
    return num1 * factor
print(multiple_of_number(10))       
