Bio=["Asmitha",18,"Bangalore"]
print("List values:", Bio)
print(type(Bio))


#adding values to list
Bio.append("Engineer")
print( Bio)


#checking the length of list
print("Length of list:", len(Bio))


#adding values to list at specific index
Bio.insert(1,"Female")
print(Bio)

#replace values in list
Bio[4]="Python"
print(Bio)


#removing values from list
Bio.remove("Bangalore") 
print(Bio)
Bio.pop(2) #removing value at index 2
print(Bio)

#reversing the list
print("Before reversing:", Bio)
Bio.reverse()
print("After reversing:", Bio)

#min, max, sum of list
salary=[10000,20000,30000,40000]
print(min(salary))
print(max(salary))
print(sum(salary))
print(salary)

#copy,count
list=[1,2,3,4,5 ]
copy=list.copy()
print("copy of list:", copy)
count=list.count(3)
print("count of 3 in list:", count)

#getting list values in run time
li=input("enter the list values")
list=li.split(",") #splitting the input string into list using comma as separator
print("List values:",list)
for i in list:
    print(i)
    
#looping list
n=int(input("enter the list"))
empty_list=[]
for i in range(n):
    livalue=input("enter the list values")
    empty_list.append(livalue)
print("List values:", empty_list)