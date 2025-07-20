try:
    num1, num2 = eval(input("Enter two numbers that are separated by a comma:"))
    result = num1 / num2
    print("The result is", result)

except ZeroDivisionError:
    print("Division by 0 is a error")

except SyntaxError:
    print("The comma is missing. Please enter numbers like this. 1,2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")