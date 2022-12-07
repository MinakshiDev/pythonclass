# for(int i=0;i<10;i++)->this is not available in python
#a=[1, 2, 3, 4,5]
#for i in a:
    #print(i)
#range(start,stop,step)
#range(10)-> start=0,stop=9,step=1 
#for i in range(1,101):
    #print(i)
#total=0

#for i in range(1,101):
    #total=total + i
#print(total)
#print(sum([1, 2, 3, 4, 5]))
#print(sum(range(1,101)))

#print sum of multiples of 3 from 1 to 100
#total=0
#for i in range(3,101,3):
    #total += i
#print(total)  

#print sum of multiples of 3 or 5 from 1 to 100
#total=0
#for i in range(0,100):
    #if i%3==0 or i%5==0:
        #total += i
    
#print(total)  

#while loop
#a = 1
#while a<10:
    #print(f"I am inside loop for {a} times.")
    #a=a+1

#task
#username=input("enter your username:")
#password=input("enter your password:")
#while username != "abc@gmail.com" or password != "12345":
    #username=input("enter your username:")
    #password=input("enter your password:")
#print("success")  

#a= ["ram", "shyam", "sita", "hari", "gita"]
#output=[]
#for i in a:
    #output.append(i.capitalize())
#print(output)
#task2

# emails= ["1@gmail.com", "2@gmail.com", "3@yahoo.com", "4@gmail.com", "5@outlook.com", "6@yahoo.com"]
# output=[]
# for i in emails:
#     if i.endswith("@gmail.com"):
#         output.append(i)
    
# print(output)    

#break, continue

for i in range(1,10):
    if i%7==0:
        break
    print(i)

for i in range(1,10):
    if i%7==0:
        continue
    print(i)

    

