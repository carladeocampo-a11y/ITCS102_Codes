from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Username ---> ")
    password = getpass("Password ---> ")

    if username == "carla1" and password == "eunice1" :
        print("Acces Granted")
        isLogin = True
    else:
        print("Access Denied")
        isLogin = False