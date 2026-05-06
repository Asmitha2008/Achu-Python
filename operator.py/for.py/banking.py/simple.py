print("Banking System")
print("Please place your ATM card and enter your account number.")
account=int(input("Enter your account number: "))
amount=int(input("Enter the amount in your account: "))
withdraw=int(input("Enter the amount you want to withdraw: "))
if withdraw>amount:
    print("Insufficient balance")
else:
    print("You have withdrawn rupees",withdraw)
    print("Your remaining balance is",amount-withdraw)
deposit=int(input("Enter the amount you want to deposit: "))
if deposit<0:
    print("Invalid amount")
else:
    print("you have deposited rupees",deposit)
    print("Your remaining balance is",amount-withdraw+deposit)