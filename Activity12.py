import getpass

username = 'carla_'
password = 'de_ocampo'

u = input("Enter Username ---> ")
p = getpass.getpass("Enter Password ---> ")

if username == u and password == p :
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")