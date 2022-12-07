name = input("enter your name:")
your_class = input("ente your class:")
rollnumber = input("enter your roll number:")
english = int(input("enter your marks in english:"))
maths = int(input("enter your marks in maths:"))
science = int(input("enter your marks in science:"))
while english > 100 or maths>100 or science>100:
    print("you enter more than 100")
    if english >100:
        english = int(input("enter your marks in english:"))
    if maths>100:
        maths = int(input("enter your marks in maths:"))
    if science>100:
        science = int(input("enter your marks in science:"))

total_marks=300
obtained_marks= int(english)+int(maths)+int(science)
percentage=obtained_marks/total_marks*100 
print("Your name is ",name)
print("Your class is ",your_class)
print("Your rollnumber is",rollnumber)
print("Your marks in English is",english)
print("Your marks in Maths is",maths)
print("Your marks in Science is",science)
print("obtained_marks is",obtained_marks)
print("percentage is",percentage,"%")