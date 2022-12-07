# name = input("enter your name:")
# your_class = input("enter your class:")
# rollnumber = input("enter your roll number:")
# english = input("enter your marks in english:")
# maths = input("enter your marks in maths:")
# science = input("enter your marks in science:")
# total_marks=300
# obtained_marks= int(english)+int(maths)+int(science)
# percentage=obtained_marks/total_marks*100
# if percentage<40:
#     print(" you are fail")
# else:
#     print(" you are pass")

# print("Your name is ",name)
# print("Your class is ",your_class)
# print("Your rollnumber is",rollnumber)
# print("Your marks in English is",english)
# print("Your marks in Maths is",maths)
# print("Your marks in Science is",science)
# print("obtained_marks is",obtained_marks)
# print("percentage is",percentage,"%")


# students_score = [
#     {"name": "Ram", "score": 80}
#     {"name": "Sita", "score": 100}
#     {"name": "Abc", "score": 35}
#     {"name": "xyz", "score": 40}
#     {"name": "John", "score": 37}
#     {"name": "Shyam", "score": 90}
#     {"name": "Hari", "score": 36}
# ]

# out = []
# for i in students_score:
#     score = i.get("score")
#     if score >= 40:
#         out.append(i)
# # print(out)

# output = list(filter(lambda i:i.get("score")>=40, students_score))
# print(output)

colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
remove = ["yellow", "red"]

colors_copy = colors.copy()
for i in colors_copy:
    if i in remove:
        colors.remove(i)
print(colors)


colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]

color_1 = input("Enter a color: ")
color_2 =input("Enter another color: ")
remove = [color_1, color_2]
print(list(filter(lambda i: i not in remove,colors)))
