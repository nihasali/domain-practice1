# polymorphism method overriding

class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def summ(self):
        print(self.a + self.b)
class Subtraction(Addition):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def summ(self):
        print(self.a - self.b)
obj=Subtraction(10,5)
obj.summ()


class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def summ(self):
        print(self.a + self.b)


class Subtraction(Addition):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summ(self):
        super().summ()    # Calls Addition.summ()
        print(self.a - self.b)

obj = Subtraction(10,5)
obj.summ()

class addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def summ(self):
        print(self.a+self.b)
class subtraction(addition):
    def __init__(self,a,b):
        super().__init__(a,b) # to acess attributes from parent
    def summ(self):
        super().summ() # to acess method from parent
        print(self.a-self.b)

obj=subtraction(10,5)
obj.summ()

# single inheritance
class person:
    def __init__(self,name):
        self.name=name
    
class Employee(person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary

emp=Employee("John",5000)
print(emp.name,emp.salary)

class job:
    def __init__(self,salary):
        self.salary=salary
class employeepersonjob(Employee,job):  # multiple inheritance
    def __init__(self,name,salary):
        Employee.__init__(self,name,salary)
        job.__init__(self,salary)
emp2=employeepersonjob("Alice",6000)
print(emp2.name,emp2.salary)


class manager(employeepersonjob): #multilevel inheritance
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department


mgr=manager("Bob",8000,"HR")
print(mgr.name,mgr.salary,mgr.department)


class assistantmanager(employeepersonjob): # heierichal inheritance0

    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size
    
asst_mgr=assistantmanager("Charlie",9000,10)
print(asst_mgr.name,asst_mgr.salary,asst_mgr.team_size)


abstarction
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class car(Vehicle):
    def start_engine(self):
        print("Car engine strated with key")
class bike(Vehicle):
    def start_engine(self):
        print("Bike engine start with button")
        
c=car()
b=bike()
c.start_engine()
b.start_engine()


class Employee:
    def __init__(self):
        self.__salary=50000
    def get_salary(self):
        return self.__salary
        
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
        else:
            print("invalid salary")
            
emp=Employee()
print(emp.get_salary())
emp.set_salary(60000)
print(emp.get_salary())


class BankAccount:
    def __init__(self):
        self.balance=1000
    def _show_balance(self):
        print(f"Balance:{self.balance}")
    def __update_balance(self,amount):
        self.balance+=amount
   
    def deposit(self,amount):
        if amount>0:
           self.__update_balance(amount)
           self._show_balance()
        else:
            print("invalid amount")
account=BankAccount()
account._show_balance()
account.deposit(500)