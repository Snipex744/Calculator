import math
import time
import re
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

special_chars = r"[!@#$%^&*()_+={}|\[\]<>?~-]"

print("[1] Add           [2] Subtract")
print(" ")
print("[3] Multiply      [4] Divide")
print(" ")
print("[5] Square root")
print(" ")

question = input("What do you wanna do?: ").lower().strip()

while question != "add" and question != "1" and question != "subtract" and question != "2" and question != "multiply" and question != "3" and question != "divide" and question != "4" and question != "square root" and question != "5":
	print("INVALID")
	print("")
	question = input("What do you wanna do?:").lower().strip()

while question == "add" or question == "1":
    a = input("First number: ")
    b = input("Second number: ")
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif re.search(special_chars, a) or re.search(special_chars, b):
    	print("INVALID")
    	print("")
    elif float(a) == 0 and float(b) == 0:
    	face()
    	print("")
    else:
    	addition = float(a) + float(b)
    	print(addition)
    	print("")
while question == "subtract" or question == "2":
    a = input("First number: ")
    b = input("Second number: ")
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif re.search(special_chars, a) or re.search(special_chars, b):
    	print("INVALID")
    	print("")
    elif float(a) == 0 and float(b) == 0:
    	face()
    	print("")
    else:
    	subtraction = float(a) - float(b)
    	print(subtraction)
    	print("")
while question == "multiply" or question == "3":
    a = input("First number: ")
    b = input("Second number: ")
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif re.search(special_chars, a ) or re.search(special_chars, b):
    	print("INVALID")
    	print("")
    elif float(a) == 0 and float(b) == 0:
    	face()
    	print("")
    else:
    	multiplication = float(a) * float(b)
    	print(multiplication)
    	print("")
while question == "divide" or question == "4":
    a = input("First number: ")
    b = input("Second number: ")
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif re.search(special_chars, a) or re.search(special_chars, b):
    	print("INVALID")
    	print("")
    elif float(b) == 0:
    	face()
    	print("")
    else:
    	division = float(a) / float(b)
    	print(division)
    	print("")
while question == "square root" or question == "5":
	a = input("What number: ")
	a = a.replace(" ", "")
	if str(a).isalpha() == True:
		print("INVALID")
		print("")
	elif re.search(special_chars, a):
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