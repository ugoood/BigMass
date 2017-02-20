# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def set_age(self, age):
#         self.age = age
#     def set_major(self, major):
#         self.major = major

# anna = Student('anna')
# anna.set_age(21)
# anna.set_major('CS')
# print(anna.major)

# class MasterStudent(Student):
#     internship = 'hehehe'
    
    
#     def __init__(self, name):
#         self.name = name + "aa"


# # james = MasterStudent('james', 18)
# james = MasterStudent('james')
# print(james.internship)
# print(james.name)
# james.set_age(33)
# print(james.age)

# class C1():
#     def p1():
#         print("I am C1")

# class C2():
#     def p2():
#         print("I am C2")


# class C(C1, C2):
#     pass

# cc = C()
# cc.p1()

# class Student():
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score

#     def print_score(self):
#         print('%s : %s' %(self.__name, self.__score))

# s = Student("Peter", 98)
# s.print_score()
# # s.__name          #AttributeError
# print(s._Student__name)     # right, no any private

class Animal():
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

# j = isinstance(h, Husky)    # True
# print(j)
# j = isinstance(h, Animal)   # True
# print(j)            
# j = isinstance(a, Dog)  # False
# print(j)
j = isinstance([1, 2, 3], (str, list))
print(j)