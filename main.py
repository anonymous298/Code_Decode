def display():
    name = input("Enter your name: ")
    print(f"Welcome {name}")

    while True:

        user = int(input("1 for code 2 for decode 0 to quit: "))

        if user == 1:
            code()

        elif user == 2:
            decode()

        elif user == 0:
            break

        else:
            print("enter above options!")

def code():
    user = input("Enter your message here: ")
    split = user.split()
    r1 = "tsd"
    r2 = "zfa"
    lst = []

    for i in split:

        if len(user) > 3:

            code = r1 + i[1:] +i[0] + r2
            lst.append(code)
        
        else:
            code = i[::-1]
            lst.append(code)

    print(" ".join(lst))

def decode():
    user = input("Enter your message here: ")
    split = user.split()
    lst = []

    for i in split:
        if len(user) > 3:
            removal = i[3:-3]
            decode = removal[-1] + removal[:-1]
            lst.append(decode)

        else:
            decode = i[::-1]
            lst.append(decode)

    print(" ".join(lst))

display()