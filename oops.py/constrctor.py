class car:
    def __init__(self,brand,name):
        self.brand=brand
        self.name=name
        print("brand",brand,"name",name)
c1=car("audi","a4")
        
 
class car:
    def __init__(self,brand,name):
        print("brand",brand,"name",name)
c1=car("audi","a4")
        
 
class car:
    def __init__(self,brand,name):
        self.brand=brand
        self.name=name
        print("brand",brand,"name",name)
    def display(self):
        print("brand",self.brand,"name",self.name)
c1=car("audi","a4")
c2=car("bmw","x5")
c2.display()
c1.display()


class school:
    def __init__(self,standard,sec):
        self.standard=standard
        self.sec=sec
        print("standard",standard,"sec",sec)
    def display(self):
        print("standard",self.standard,"sec",self.sec)
s1=school(int(input("enter the standard")),input("enter the sec"))
s2=school("9th","b")