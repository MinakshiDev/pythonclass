#out=[2, 4, 6, 8, 10]
# a=[1,2,3,4,5,6,7,8,9,10]
# def is_even(num):
#     return num%2==0
    
# out=filter(lambda num:num % 2==0, a)
# print(list(out))

emails= ["1@gmail.com", "2@gmail.com", "3@yahoo.com", "4@gmail.com", "5@yahoo.com","6@outlook.com"]

def a(mail):
    return mail.endswith("@gmail.com")
out=filter(lambda mail:mail.endswith("@gmail.com"),emails)
# print(list(out))


d=[17, 20, 25, 30]
#print(sum(d)) 

c=["17","20","25","30"]
total=0
for i in c:
    total= total + int(i)
#print(total)

b="12d57d54d90"
# print(b.split("d"))
a=b.split("d")
total=0
for i in a:
    total= total + int(i)
#print(total) 

a="457d89e36"
total=0
for i in a:
    if i.isnumeric():
        total=total+int(i)
print(total) 
# print(sum(map(int,filter(lambda v:v.isnumeric(),a))))       














