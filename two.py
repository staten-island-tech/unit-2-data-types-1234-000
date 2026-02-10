num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

for i in range(1, num1 + 1):
    if i <= num2:
        if num1%i==0 and num2%i==0:
            gcf = i
            
print ("Factors are", gcf)



        