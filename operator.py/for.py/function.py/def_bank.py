balance=[1000,5000,8000,10000]
def debit(money=0,pos=0):
    if money <= balance[pos]:
        balance[pos]-=money
        print(money,"withdrawn")
        return balance[pos]
    else: print("cannot debit")
bank=debit(1000,1)
print(bank,"remaining balance")


#new
balance=[1000,5000,8000,10000]
def debit(money=0,pos=0):
    if money <= balance[pos]:
        balance[pos]-=money
        print(money,"withdrawn")
    else: print("cannot debit")
debit(1000,1)
