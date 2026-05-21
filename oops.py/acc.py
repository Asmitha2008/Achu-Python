class Account:
    #constrcutor
    def __init__(self,name="",num=0,bal=0.0):
        print("Constructor called")
        self.__holder=name
        self.__accNum=num
        self.__accBal=bal
    def __add__(self, other):
        self.__accBal+=other
        print(other,"credited",self.__accNum)
    def __sub__(self, other):
        if self.__accBal>=other:
            self.__accBal-=other
            print(other,"debited",self.__accNum)
        else:
            print(self.__accNum,"Insufficeint_balance")
    def __str__(self):
        return self.__holder+"\n"+str(self.__accNum)+"\n"+str(self.__accBal)+"\n"
    def setHolder(self, name=""):
        self.__holder = name 
    def getHolder(self):
        return self.__holder
    def setAccNum(self,num=0):
        self.__accNum=num
    def getAccNum(self):
        return self.__accNum
    def setAccBal(self,bal=0.0):
        self.__accBal=bal
    def getAccBal(self):
        return self.__accBal
acc1=Account()
acc1.setAccNum(124523) 
acc1.setAccBal(1500.0)
acc1.setHolder("Gowthami") 
print(acc1)
acc1+5000
print(acc1)
         



