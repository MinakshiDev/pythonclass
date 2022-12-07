# try:
#     #code
# except Exception:catch specific error or exception
#     #code
# except Exception:catch specific error or exception
#     #code
# else:
#     #code
# finally:
#     #code    

try:
    a=int(input("Enter any number:"))
    b=int(input("Enter anoter number:"))
except ValueError:
    print("cannot convert to integer")
else:        
    sum=a+b
print("sum of two number",sum)

name=input("Enter name:")
print(name)


