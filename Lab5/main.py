import math

print("Exercitiul 1")
print("")
class Forma:
    def printName(self): pass
    def getAria(self): pass
    def getPerimetrul(self): pass

class Circle(Forma):
    def __init__(self,r):
        self.r = r

    def getName(self): return "cerc"

    def getRaza(self):
        return self.r

    def getAria(self):
        if(self.r != None):
            return (math.pi) * self.r ** 2
        return None

    def getPerimetrul(self):
        if (self.r != None):
            return 2 * (math.pi) * self.r
        return None

class Rectangle(Forma):
    def __init__(self,l,L):
        self.l = l
        self.L = L

    def getName(self): return "dreptunghi"

    def getLungime(self):
        return self.l

    def getLatime(self):
        return self.L

    def getAria(self):
        if (self.l != None and self.L != None):
            return  self.l * self.L
        return None

    def getPerimetrul(self):
        if (self.l != None and self.L != None):
            return (self.l + self.L) * 2
        return None

class Triangle(Forma):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def getName(self): return "triunghi"

    def getFirstSide(self):
        return self.a

    def getSecondSide(self):
        return self.b

    def getThirdSide(self):
        return self.c

    def getAria(self):
        if (self.a != None and self.b != None and self.c != None):
            s = (self.a + self.b + self.c)/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return None

    def getPerimetrul(self):
        if (self.a != None and self.b != None and self.c != None):
            return self.a + self.b + self.c
        return None

figura1 = Circle(6)
print("Prima figura este un", figura1.getName(), "cu perimetrul ", figura1.getPerimetrul(), " si aria ", figura1.getAria(), ".")

figura2 = Rectangle(6,8)
print("A doua figura este un", figura2.getName(), "cu perimetrul ", figura2.getPerimetrul(), " si aria ", figura2.getAria(), ".")

figura3 = Triangle(7,8,9)
print("A treia figura este un", figura3.getName(), "cu perimetrul ", figura3.getPerimetrul(), " si aria ", figura3.getAria(), ".")
print("")

# Exercitiul 2

print("Exercitiul 2")
print("")

class Account:
    def __init__(self,sold=0.0):
        self.sold = sold

    def getSold(self):
        return self.sold

    def deposit(self,suma):
        if suma > 0:
            self.sold += suma
        else: print("Invalid amount.")

    def withdrawal(self,suma):
        if suma > 0 and suma < self.sold:
            self.sold -= suma
        else: print("Invalid amount.")

    def calculate_interest(self): pass

class SavingAccount(Account):
    def __init__(self,sold=0.0):
        self.sold = sold

    def calculate_interest(self,rata, timp):
        if timp > 0 :
            if rata > 0:
                return self.sold * rata * timp
            else:
                print("Invalid rate.")
        else: print("Invalid time.")

class CheckingAccount(Account):
    def __init__(self, sold=0.0,limit=0.1):
        self.sold = sold
        self.limit= limit

    def withdrawal(self, suma):
        if suma > 0 and suma <= (self.sold + self.limit) :
            self.sold -= suma
        else:
            print("Invalid amount.")

cont1 = SavingAccount(500)
cont1.deposit(500)
cont1.withdrawal(150)
print("Contul curent are depozitat ", cont1.getSold(), " de lei.")
print("Pentru o rata de 0.4 interesul este de ", cont1.calculate_interest(0.4,1), " de lei pe an.");

cont2 = CheckingAccount(300,200)
cont2.deposit(400)
cont2.withdrawal(150)
print("Contul curent are depozitat ", cont2.getSold(), " de lei.")
cont2.withdrawal(751)
print("")

# Exercitiul 3

print("Exercitiul 3")
print("")

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def print(self):
        print(f'Marca: {self.make} ; Model: {self.model} ; Anul: {self.year}')

class Car(Vehicle):
    def __init__(self,make,model,year,fuel):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel

    def getFuel(self):
        return self.fuel

    def calculate_mileage(self,distance):
        return distance / self.fuel

class Motocycle(Vehicle):
    def __init__(self, make, model, year, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel

    def getFuel(self):
        return self.fuel

    def calculate_mileage(self,distance): # miles / gal.
        return distance / self.fuel
class Truck(Vehicle):
    def __init__(self,make,model,year, gcvwr, curb_weight): # GCVWR= gross combined vehicle weight rating
        self.make = make
        self.model = model
        self.year = year
        self.gcvwr = gcvwr
        self.curb_weight = curb_weight

    def getGCVWR(self):
        return self.gcvwr

    def getCurbWeight(self):
        return self.curb_weight

    def calculate_towing_capacity(self):
        return self.gcvwr - self.curb_weight

masina = Car("Nissan"," 350Z",2004,20)
masina.print()
print(f'Mileage for 100 miles: {masina.calculate_mileage(100)}')

motocicleta = Motocycle("Suzuki","SV650",1999,3)
motocicleta.print()
print(f'Mileage for 100 miles: {motocicleta.calculate_mileage(100)}')

camion = Truck("Freightliner","Cascadia ",2009,52000,27487)
camion.print()
print(f'Towing capacity: {camion.calculate_towing_capacity()} kg')
print("")

# Exercitiul 4

print("Exercitiul 4")
print("")

class Employee:
    def __init__(self,name,ID,salary,role):
        self.name = name
        self.ID = ID
        self.salary = salary
        self.role = role

    def info(self):
        print(f'Name: {self.name} ; Id: {self.ID} ; Salary: {self.salary} ; Role: {self.role}')

class Manager(Employee):
    def __init__(self, name, ID, salary, department):
        super().__init__(name, ID, salary, "Manager")
        self.department = department

    def program_meeting(self, date, hour):
        print(f'Meeting programmed for {date}, at {hour} o clock.')

    def run_meeting(self):
        pass

    def info(self):
        super().info()
        print(f'Department: {self.department}')

class Engineer(Employee):
    def __init__(self,name,ID,salary,programming_language):
        super().__init__(name,ID,salary,"Engineer")
        self.programming_language = programming_language
        self.lines_written = 0

    def coding(self,lines):
        self.lines_written += lines

    def info(self):
        super().info()
        print(f'Programming language: {self.programming_language}')
        print(f'Total of written lines: {self.lines_written}')

class Salesperson(Employee):
    def __init__(self, name, ID, salary):
        super().__init__(name, ID, salary, "Salesperson")
        self.sales = 0

    def sell(self, amount):
        self.sales += amount

    def info(self):
        super().info()
        print(f'Sales: {self.sales}$')

manager = Manager("Joe Biden",1001, 1000,"Sales department")
manager.program_meeting("2023-11-16",9)
manager.run_meeting()
manager.info()
print("")

engineer = Engineer("Kim Jungwoo", 1002,550,"Python")
engineer.coding(100)
engineer.coding(1000)
engineer.info()
print("")

salesperson = Salesperson("Grecu Silviu Andrei",1003,450)
salesperson.sell(100)
salesperson.sell(200)
salesperson.info()
print("")

# Exercitiul 5

print("Exercitiul 5")
print("")

class Animal:
    def __init__(self,name):
        self.name = name

class Mammal(Animal):
    def __init__(self,name,habitat, food_type, has_tail,horn_number):
        self.name = name
        self.habitat = habitat
        self.diet = food_type
        self.tail = has_tail
        self.horns = horn_number

    def run(self): pass

    def give_birth(self): pass

class Bird(Animal):
    def __init__(self,name,habitat,feather_colors,sings):
        self.name = name
        self.habitat = habitat
        self.colors = feather_colors
        self.sings = sings

    def fly(self): pass

    def lay_eggs(self): pass

class Fish(Animal):
    def __init__(self,name,habitat,water_type,fins):
        self.name = name
        self.habitat = habitat
        self.water_type = water_type
        self.fins = fins
    def swim(self): pass
    def lay_eggs(self): pass

goat = Mammal("goat","hills","herbivore",True,2)
goat.run()
goat.give_birth()
print(f'The {goat.name} lives on {goat.habitat}, it is a {goat.diet} and it has {goat.horns} horns.')
if(goat.tail):
    print(f'The {goat.name} has a tail.')
else:
    print(f'The {goat.name} does not have a tail.')

pelican = Bird("pelican","coast", "white",False)
pelican.fly()
pelican.lay_eggs()
print(f'The {pelican.name} lives on {pelican.habitat} and its feathers are {pelican.colors}.')
if(pelican.sings):
    print(f'The {pelican.name} can sing.')
else:
    print(f'The {pelican.name} cannot sing.')

goldfish = Fish("goldfish","ocean","seawater",7)
goldfish.swim()
goldfish.lay_eggs()
print(f'The {goldfish.name} lives in the {goldfish.habitat}. It prefers {goldfish.water_type} and it has {goldfish.fins} fins.')
print("")

# Exercitiul 6

print("Exercitiul 6")
print("")

from datetime import date
from datetime import timedelta
class LibraryItem:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.return_date = None
        self.check_out = False

    def info(self):
        print(f'Title: {self.title} ; Author: {self.author}')
        if self.check_out:
            print(f'Checked out. Must be returned until {self.return_date}.')

    def checkOut(self,days):
        if self.check_out:
            print(f'{self.title} already checked out.')
        else:
            self.check_out = True
            self.return_date = date.today() + timedelta(days = days)
            print(f'Item checked out. Do not forget to return it until {self.return_date}.')

    def returnItem(self):
        if self.check_out:
           if (date.today() - self.return_date).days > 0:
               print("You are late. Thanks for returning the item tho.")
           else:
               print("Item returned.")
           self.check_out = False
           self.return_date = None
        else:
            print(f'{self.title} not checked out.')


class Book(LibraryItem):
    def __init__(self,title,author,genre):
        super().__init__(title,author)
        self.genre = genre

    def info(self):
        super().info()
        print(f'Genre: {self.genre}')

class DVD(LibraryItem):
    def __init__(self, title, author, length):
        super().__init__(title, author)
        self.length = length

    def info(self):
        super().info()
        print(f'Movie length: {self.length}')


class Magazine(LibraryItem):
    def __init__(self, title, author, edition_number, pages):
        super().__init__(title, author)
        self.edition_number = edition_number
        self.pages = pages

    def info(self):
        super().info()
        print(f'Edition: {self.edition_number}')
        print(f'Number of pages: {self.pages}')

book = Book("Loki: Where Mischief Lies","Mackenzi Lee","fantasy")
book.info()
book.returnItem()
book.checkOut(21)
book.returnItem()
print("")
dvd = DVD("Avatar","James Cameron",162)
dvd.checkOut(7)
dvd.info()
dvd.returnItem()
print("")
magazine = Magazine("Mineralele Pamantului","Colectii Libertatea","Editia nr. 08",25)
magazine.checkOut(14)
magazine.info()
magazine.returnItem()