# class Student:
#     def __init__(self):
#         self.name ='Chiru'
#         self.batch_no ='01'
#         print('this is a instance method/constructor')
#         '''This is coming from the instance method'''
#     def display(self):
#         print("Name is",self.name)
#         print('batch is',self.batch_no)
#
# # Student()
# #Student().display()
#
# obj = Student().display('Chinnaswamy','02')
# print(obj)


# class Student:
#     def __init__(self):
#         self.name ='Chiru'
#         self.batch_no ='01'
#         print('this is a instance method/constructor')
#         '''This is coming from the instance method'''
#     def display(self):
#         print("Name is",self.name)
#         print('batch is',self.batch_no)
#
# s1 = Student()# here S1 is the reference variable using it we are accessing the class related methods and variables
# print('this is name', s1.name)
# print('this is the batch_no',s1.batch_no)
# s1.display()  # calling display method using s1 as the reference variable
# s1.__init__()

# class GFG:
# 	def __init__(self, name, company):
# 		self.name = name
# 		self.company = company
#
# 	def __str__(self):
# 		return f"My name is {self.name} and I work in {self.company}."
#
#
# my_obj = GFG("John", "GeeksForGeeks")
# print(my_obj)

##################################################################################################################################

############11-10-23###################
#
# class Student:
#     def __init__(self):
#         self.name ='Chiru'
#         self.batch_no ='01'
#         print('this is a instance method/constructor')
#         '''This is coming from the instance method'''
#     def display(self):
#         print("Name is",self.name)
#         print('batch is',self.batch_no)
#
# s1 = Student()# here S1 is the reference variable using it we are accessing the class related methods and variables
#
# s1.__init__()
############################################################################
class Test:
    def __init__(self):
        print('the id of self is ',id(self))
    def display(self):
        print('this is test method')

obj = Test()#here obj is reference variable to the Test() object
print('the object obj is',id(obj))
