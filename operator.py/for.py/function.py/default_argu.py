def register(name,location,prefix="Ms.",suffix="B.E,M.E(HR in ZOGO)"):
    if location=="SWITZERLAND":
        print(prefix,name,"with the qualification",suffix,"welcome to food fest at our college in",location)
    elif location=="LONDON":
        print(prefix,name,"with the qualification",suffix,"welcome to food fest at our college in",location)
    else:
        print(prefix,name,"with the qualification",suffix,"you are eligibile as our guest",location)    
register("ASWATHI.S","SWITZERLAND")  
register("ASMITHA.S.R","LONDON") 
register("ASMI","CANADA")
register("SWITZERLAND","ASWATHI.S")