def thing():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if (username == "Yusuf5" and password == "33kk") or (username == "Mary80" and password == "af5r"):
            print("Access granted")
            break
        else:
            print("Access denied")

thing()
