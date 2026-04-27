#billing
price=float(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity of the item: "))
total=price*quantity
Tax=10
tax_percentage=(total*Tax)/100
final_amount=total+tax_percentage
print("The total amount is:",total)
print("The final amount is:",final_amount)
print("The tax amount is:",tax_percentage )