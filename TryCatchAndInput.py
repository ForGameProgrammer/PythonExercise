name = str(input("Enter Your Name : ")) # str = converts numbers to string
print("Hello", name)

while True: # Infinite Loop
    try:
        number = int(input("Enter a Number : ")) # int = Converts to Number (integer) returns ValueError if enter string
        print(number)
        break
    except:
        print("Please Enter Valid Number")