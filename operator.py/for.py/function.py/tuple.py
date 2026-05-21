Name=("Asmitha","Asmitha","Asmitha","Aswathi","Dhanya","Aishwarya",22,22)
print("Tuple values:", Name)
print(type(Name))

#slicing tuple
print("Sliced tuple:", Name[0:4])
print("Sliced tuple:", Name[:4])
print("Sliced tuple:", Name[2:])
print("Sliced tuple:", Name[4:8:2])

#method
tuple=("munch","kitkat","diary milk","galaxy","munch","galaxy")
value=tuple.count("munch")
print(value)
value1=tuple.index("kitkat")
print(value1)

#append method
clg=("psg","kct","vit","iit","nit")
clg1=list(clg)
clg1.append("kiot")
clg=tuple(clg1)
print(clg)

#insert
colors=('blue','green','red','yellow')
colorss=list(colors)
colorss.insert(1,'grey')
colors=tuple(colorss)
print(colors)


#adding tuple to tuple
data=('Cat','Dog','dhanya')
data1=('aswathi',)
data+=data1
print(data)

#loop tuple
a=('hi','hello','what')
for i in range(len(a)):
    print(a[i])
    
for i in a:
    print(a)
    
    
#adding
place=('kerala','telgana','salem')
place1=(1,2,3)
result=place+place1
print(result)

#join
place=('salem','madurai','chennai')
join=place*4
print(join)