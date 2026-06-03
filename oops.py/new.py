# class college:
#     def __init__(self,name,course):
#         self.n=name
#         self.c=course
#     def display(self):
#         print("name",self.n,"course",self.c)
# c1=college("sri chaitanya","mca")
# c1.display()


# #single inheritance
# class car:
#     def steering(self):
#         print("comfortable ride")
# class bike (car):
#     def seat (self):
#         print("two wheeler")
# b1=bike()
# b1.steering()
# b1.seat()


#multilevel inheritance
# class car:
#     def steering(self):
#         print("comfortable ride")
# class bike (car):
#     def seat (self):
#         print("two wheeler")
# class cycle (bike):
#     def pedal(self):
#         print("manual")
# c1=cycle()
# c1.steering()       
# c1.seat()
# c1.pedal()

# #hierarchical inheritance
# class school:
#     def teacher(self):
#         print("GOOD MORNING")
# class student(school):
#     def study(self):
#         print("STUDY HARD")
# class staff(school):
#     def work(self):
#         print("WORK HARD")
# class principal(school):
#     def office(self):
#         print("OFFICE WORK")
# d1=school()
# d1.teacher()
# s1=student()
# s1.study()
# d2=staff()
# d2.work()
# s2=principal()
# s2.office()

# # #multiple inheritance
# class Travels():
#     def bus(self):
#         print("bus is on time")
# class Travels1():
#     def train(self):
#         print("train is on time")
# class main(Travels,Travels1):
#     def flight(self):
#         print("flight is on time")
# m1=main()
# m1.bus()
# m1.train()  
# m1.flight()

##multiple inheritance
# class supermarket():
#     def vegetables(self):
#         print("vegetables are fresh")
# class supermarket1():
#     def fruits(self):
#         print("fruits are not fresh")
# class supermarket2():
#     def dairy(self):
#         print("dairy products are fresh")
# class supermarket3():
#     def bakery(self):
#         print("bakery products are not fresh")
# class main(supermarket,supermarket1,supermarket2,supermarket3):
#     def grocery(self):
#         print("grocery products are fresh")
# m1=main()
# m1.vegetables() 
# m1.fruits()
# m1.dairy()
# m1.bakery()
# m1.grocery()

# class mobile:
#     __model=""#private variable,only  small letter and __ is used
#     __price=0.0
#     __ram=0
#     __internal=0
#     def setModel(self,mod=0):#gettersetter method
#         self.__model=mod
#     def getModel(self):
#         return self.__model
#     def setPrice(self,pri=0.0):
#         self.__price=pri
#     def getPrice(self):
#         return self.__price
#     def setRam(self,ram=''):
#         self.__ram=ram
#     def getRam(self):
#         return self.__ram
#     def setInternal(self,internal=0):
#         self.__internal=internal
#     def getInternal(self):
#         return self.__internal
# m1=mobile()
# m1.setModel(input("enter model"))
# m1.setPrice(float(input("enter price")))
# m1.setRam(input("enter ram"))
# m1.setInternal(int(input("enter internal storage")))
# print("your bill is generated")
# print("model",m1.getModel())
# print("price",m1.getPrice())
# print("ram",m1.getRam())
# print("internal storage",m1.getInternal())
# print("thanku for shopping")



# #abstract class
# from abc import ABC
# class bus (ABC):
#     def volvo(self):
#         print("luxury bus")
# class lorry(bus):
#     def volvo(self):
#         print("heavy vehicle")
# class car(lorry):
#     def volvo(self):
#         print("luxury car")
# b=bus()
# b.volvo()
# l=lorry()
# l.volvo()
# c=car()
# c.volvo()


#polymorphism
# class bank:
#     def interest(self):
#         print("interest is 5%")
# class sbi(bank):
#     def interest(self):
#         print("interest is 6%")
# class hdfc(bank):
#     def interest(self):
#         print("interest is 7%")
# b1=bank()
# b1.interest()
# b1.interest()
# b1.interest()
hgfhjgkjhjklhkjhkjhjmkhjh


#polymorphism2
# class shop:
#     def bill(self):
#         print("bill is generated")
# class shop1(shop):
#     def bill(self):
#         print("bill is generated with discount")
# class shop2(shop):
#     def bill(self):
#         print("bill is generated with no discount")
# s1=shop()
# s2=shop1()
# s3=shop2()
# s1.bill()
# s2.bill()