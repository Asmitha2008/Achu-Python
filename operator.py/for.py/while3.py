hire=5
while hire>0:
    skills=input("Enter the skills: ")
    project=int(input("Enter the project: "))
    if skills=="python" and project<=5:
        print("candidate hired")
        hire-=1
    elif skills=="java" and project>=6:
        print("candidate hired")
        hire-=1
    else:
        print("candidate not hired")
        
    #same in different way
    
hire=5
while hire>0:
    skills=input("Enter the skills: ")
    project=int(input("Enter the project: "))
    if skills=="python" and project<=5:
        print("candidate hired")
        hire-=1
    else:
        print("candidate not hired")
        
    