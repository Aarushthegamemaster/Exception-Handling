try:
    age = int(input("Please enter your age:"))
    print("Your age is", age)
    if age%2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")

except ValueError:
    print("Please restart and write your age in numbers")