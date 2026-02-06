bill = float(input("Print Bill: $"))
experience = input("How was your experience? Good / Great / Bad / Okay: ")
if experience == "Good":
        print("$",bill*1.25)
elif experience == "Great":
        print("$",bill*1.20)
elif experience == "Okay":
        print("$",bill*1.15)
elif experience == "Bad":
        print("$",bill)