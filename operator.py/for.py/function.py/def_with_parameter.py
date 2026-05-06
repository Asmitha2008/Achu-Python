def prompt(qual,ref):
    if qual == "ug"and ref == "hr":
        print("you will be eligible to join our US company.")
    elif qual == "pg" and ref == "MANAGER":
        print("you will be eligible to join our RUSSIAN company.")
    else:
        print("you are not eligible to join our company.")
prompt("ug","hr")
prompt("pg","MANAGER")
prompt(ref="hr",qual="ug")
prompt(ref="pg",qual="MANAGER")
prompt("pg","hr")