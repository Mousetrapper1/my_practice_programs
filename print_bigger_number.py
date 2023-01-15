try:
    a = int(input("please add your first number : "))
    b = int(input("please add your second number : ")) 
    if a < b:
        print(str(b) + " is bigger ")
    elif b < a: 
        print(str(a) + " is bigger ")
except(ValueError):
    print('you made a wrong input')