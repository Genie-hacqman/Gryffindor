class School:
    def __init__(self,name,population,city):
        self.name = name
        self.population = population
        self.city = city




class Student:
    def __init__(self,name,age,school):   
        self.studentname = name
        self.age = age
        self.school = school

owass = School("Opoku Ware",6000,"santasi") 

amass = School("Amass",7000,"amakom")

kass = School("Kass",5000,"asokwa")      

print(owass.population)
print(amass.population)
print(owass.name)


hackman = Student("hackman",90,"owass")

newton = Student("newton",100,"Amass")

esther = Student("esther",70,"kass")

print(hackman.studentname)
print (newton.age)