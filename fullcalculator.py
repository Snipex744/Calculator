import math
import time
def delay(sec):
	time.sleep(sec)
def face():
	print("        ⢀⣤⣤⣶⠶⠶⣶⣤⣤⡀⠀")
	delay(1)
	print("     ⢀⣴⠾⠛⠉⠀⢠⣾⣴⡾⠛⠻⣷⣄⠀")
	delay(1)
	print("   ⢶⣶⣶⣿⣁⠀⠀⠀⠀⢸⣿⠏⢀⣤⣶⣌⠻⣦⡀⠀⠀⠀")
	delay(1)
	print("   ⣴⡟⠁⢉⣙⣿⣦⡀⠀⢸⡏⣴⠟⢡⣶⣿⣧⡹⣷⡀")
	delay(1)
	print("  ⣼⠏⢀⣾⠟⠛⠛⠻⣿⡆⠀⠀⢿⣄⠀⠙⠉⠹⣷⡸⣷")
	delay(1)
	print("⢠⣿⠀⢸⡿⢿⠇⠀⠀⣾⠇⠀⣀⣈⠻⢷⣤⣤⣤⡾⠃⢹⣇")
	delay(1)
	print("⢸⣿⠀⢸⣧⣀⣀⣠⣾⢋⣴⢿⣿⡛⠻⣶⣤⣉⠁⠀⠀⠀⣿")
	delay(1)
	print("⠈⣿⠀⠀⠙⠛⠛⠋⠁⣼⣯⣀⣿⠿⠶⠟⠉⠛⢷⣄⠀⠀⣿⡇")
	delay(1)
	print(" ⣿⠀⠀⠀⠀⠀⠀⠀⣿⡏⠉⠁⠀⠀⢀⣴⢶⣄  ⢻⡇  ⢸⡇")
	delay(1)
	print(" ⢻⣇⠀⠀⠀⠀⠀⢠⡿⢀⣀⢠⣾⠷⣾⣧⡶⠿⠟⠁⠀⣾⡇")
	delay(1)
	print(" ⠈⣿⣧⡀⠀⠀⣠⣿⣷⠟⢻⣿⣷⡾⠛⠉⠀⠀⠀⠀⢀⣿")
	delay(1)
	print(" ⢹⣿⢻⣦⡀⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⣼⠏")
	delay(1)
	print(" ⠛⠀⠈⠻⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟")

print("[1] Add           [2] Subtract")
print(" ")
print("[3] Multiply      [4] Divide")
print(" ")
print("[5] Square root")
print(" ")

question = input("What do you wanna do?: ").lower().strip()

while question != "add" and question != "subtract" and question != "multiply" and question != "divide" and question != "square root" and question != "purge the heritics":
	print("INVALID")
	print("")
	question = input("What do you wanna do?:").lower().strip()

while question == "add":
    a = input("First number: ")
    b = input("Second number: ")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif float(a) == 0 and float(b) == 0:
    	face()
    	print("")
    else:
    	addition = float(a) + float(b)
    	print(addition)
    	print("")
while question == "subtract":
    a = input("First number: ")
    b = input("Second number: ")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif float(a) == 0 and float(b) == 0:
    	face()
    	print("")
    else:
    	subtraction = float(a) - float(b)
    	print(subtraction)
    	print("")
while question == "multiply":
    a = input("First number: ")
    b = input("Second number: ")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif float(a) == 0 and float(b) == 0:
    	face()
    	print("")
    else:
    	multiplication = float(a) * float(b)
    	print(multiplication)
    	print("")
while question == "divide":
    a = input("First number: ")
    b = input("Second number: ")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif float(b) == 0:
    	face()
    	print("")
    else:
    	division = float(a) / float(b)
    	print(division)
    	print("")
while question == "square root":
	a = input("What number: ")
	if str(a).isalpha() == True:
		print("INVALID")
		print("")
	elif float(a) == 0:
		face()
		print("")
	else:
		a = float(a)
		squareroot = math.sqrt(a)
		print(squareroot)
		print("")
if question == "purge the heritics":
	print("FOR THE EMPEROR!!!!!!!")