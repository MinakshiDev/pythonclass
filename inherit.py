# class person:
#     def __init__(self, name, address)
#         self.name = name
#         self.address = address

#     def profile(self):
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")  

# class student(person):
#     def __init__(self, name, address,roll_number):
#         super().__init__(name, address)
#         self.roll_number = roll_number

#     def profile(self):
#         super().profile()
#         print(f"Roll Number: {self.roll_number}")

# class teacher(person):
#     def __init__(self, name, address, designation):
#         super().__init__(name, address)
#         self.designation = designation

# s = student("Ram", "Ktm", 1)
# s.profile()

class user:
    def __init__(self, _id, username, pwd):
        self._id = _id
        self.username = username
        self.password = pwd
        
class person(user):
    def __init__(self, _id, username, pwd, name, address):
        super().__init__(_id, username, pwd)
        self.name= name
        self.address = address

    def profile(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")  

class staff(person):
    def __init__(self, _id, username, pwd, name, address,designation):
        super().__init__(_id, username, pwd, name, address)
        self.designation =designation

    def profile(self):
        print(f"Username: {self.username}")
        print(f"Id: {self._id}")
        super().profile()
        print(f"Designation: {self.designation}")
s = staff(1, "ram@gmail.com", "124", "Ram", "Ktm", "Manager")
s.profile()            

    




