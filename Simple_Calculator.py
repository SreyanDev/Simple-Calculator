#This is used to print the title at center.

title = "Simple Calculator"
print(title.center(150))



try:                #Try this code, if the input is either float or integer (True) it runs or it will skip and go into except part.

#This is used to initialize the input through the variable.

    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))

#Function add with two parameters.

    def add(a,b):
        x=a+b
        print(f"\nThe sum of two numbers is: {x}")    #This f"{}" is a formatting string and \n to give the gap.

#Function difference with two parameters.

    def sub(a,b):
        x=a-b
        print(f"\nThe difference of two numbers is: {x}")

#Function multiply with two parameters.

    def mul(a,b):
        x=a*b
        print(f"\nThe multiplication of two numbers is: {x}")

#Function divide with two parameters.

    def div(a,b):
        x=a/b
        print(f"\nThe division of two numbers is: {x:.2f}")     #This {x.2f} is used to filer out the decimal points after two numbers.

#Function mean with two parameters.

    def mean(a,b):
        x=(a+b)/2
        print(f"\nThe mean of two numbers is: {x}")

#calling the functions.

    add(a,b)
    sub(a,b)
    mul(a,b)
    div(a,b)
    mean(a,b)

except Exception as e:                  #If the try part gets error then print the exception printed below.

    print(f"{e}\n\nEnter either float or integer number.")           #\n\n skips a line.
