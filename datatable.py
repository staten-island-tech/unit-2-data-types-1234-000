age=23
isMember=False
isResident=False

def discount(age, isMember, isResident) :
    if age < 12 or age >=65 :
        print("discount avaiable")
    elif isMember or isResident == True:
        print("discount avaiable")
    else:
        print("no discount")
discount(age, isMember, isResident)