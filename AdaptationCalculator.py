import math
import re

special_chars = r"[!@#$%`¡¿^'&,…/*_+×÷=|\<>?~-]"
letters = r"[qwŵẁẃẅeęěĕəɛẹèéëēėrŕřtþťțţṭyƴŷỳýÿuụųűůŭūüûúùiịıįīïîíìoºọœőŏōøöõóòoʻpaæāąªàáãäåsṣ̌şșṣß§śŝšdðďɗḍfggʻĝģğhĥjĵǰ̣ǰkƙķl·l·lłľļĺzźżžẓ̌xx̌cçćĉčč̣vbɓnṅɲŋŉňņńñn̈m€£¥₩♧◇♡♤■□●○•°☆▪︎¤《》]"

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
    a = input("First number: ").lower().strip()
    b = input("Second number: ").lower().strip()
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif a.count("\\") >= 1 or a.count("[") >= 1 or a.count("]") >= 1 or a.count("(") >= 1 or a.count(")") >= 1 or a.count("{") or a.count("}") >= 1 or b.count("\\") >= 1 or b.count("[") >= 1 or b.count("]") >= 1 or b.count("(") >= 1 or b.count("(") >= 1 or b.count("{") >=1 or b.count("}") >= 1:
    	print("INVALID")
    	print("")
    elif str(a) == "" or str(b) == "":
    	print("INVALID")
    	print("")
    elif re.search(special_chars, a) or re.search(special_chars, b):
    	print("INVALID")
    	print("")
    elif str(a) == "." or str(b) == ".":
    	print("INVALID")
    	print("")
    elif a.count(".") > 1 or b.count(".") > 1:
    	print("INVALID")
    	print("")
    elif re.search(letters, a) or re.search(letters, b):
    	print("INVALID")
    	print("")
    elif float(a) == 0 and float(b) == 0:
    	print("KILL YOURSELF")
    	print("")
    else:
    	addition = float(a) + float(b)
    	print(addition)
    	print("")
while question == "subtract" or question == "2":
    a = input("First number: ").strip().lower()
    b = input("Second number: ").strip().lower()
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif a.count("\\") >= 1 or a.count("[") >= 1 or a.count("]") >= 1 or a.count("(") >= 1 or a.count(")") >= 1 or a.count("{") or a.count("}") >= 1 or b.count("\\") >= 1 or b.count("[") >= 1 or b.count("]") >= 1 or b.count("(") >= 1 or b.count("(") >= 1 or b.count("{") >=1 or b.count("}") >= 1:
    	print("INVALID")
    	print("")
    elif str(a) == "" or str(b) == "":
    	print("INVALID")
    	print("")
    elif re.search(special_chars, a) or re.search(special_chars, b):
    	print("INVALID")
    	print("")
    elif str(a) == "." or str(b) == ".":
    	print("INVALID")
    	print("")
    elif a.count(".") > 1 or b.count(".") > 1:
    	print("INVALID")
    	print("")
    elif re.search(letters, a) or re.search(letters, b):
    	print("INVALID")
    elif float(a) == 0 and float(b) == 0:
    	print("KILL YOURSELF")
    	print("")
    else:
    	subtraction = float(a) - float(b)
    	print(subtraction)
    	print("")
while question == "multiply" or question == "3":
    a = input("First number: ").strip().lower()
    b = input("Second number: ").strip().lower()
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    if str(a).isalpha() == True or str(b).isalpha() == True:
    	print("INVALID")
    	print("")
    elif a.count("\\") >= 1 or a.count("[") >= 1 or a.count("]") >= 1 or a.count("(") >= 1 or a.count(")") >= 1 or a.count("{") or a.count("}") >= 1 or b.count("\\") >= 1 or b.count("[") >= 1 or b.count("]") >= 1 or b.count("(") >= 1 or b.count("(") >= 1 or b.count("{") >=1 or b.count("}") >= 1:
    	print("INVALID")
    	print("")
    elif str(a) == "" or str(b) =="":
    	print("INVALID")
    	print("")
    elif re.search(special_chars, a ) or re.search(special_chars, b):
    	print("INVALID")
    	print("")
    elif str(a) == "." or str(b) == ".":
    	print("INVALID")
    	print("")
    elif a.count(".") > 1 or b.count(".") > 1:
    	print("INVALID") 
    	print("")
    elif re.search(letters, a) or re.search(letters, b):
    	print("INVALID")
    elif float(a) == 0 and float(b) == 0:
    	print("KILL YOURSELF")
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
    elif a.count("\\") >= 1 or a.count("[") >= 1 or a.count("]") >= 1 or a.count("(") >= 1 or a.count(")") >= 1 or a.count("{") or a.count("}") >= 1 or b.count("\\") >= 1 or b.count("[") >= 1 or b.count("]") >= 1 or b.count("(") >= 1 or b.count("(") >= 1 or b.count("{") >=1 or b.count("}") >= 1:
    	print("INVALID")
    	print("")
    elif str(a) == "" or str(b) == "":
    	print("INVALID")
    	print("")
    elif re.search(special_chars, a) or re.search(special_chars, b):
    	print("INVALID")
    	print("")
    elif str(a) == "." or str(b) == ".":
    	print("INVALID")
    	print("")
    elif a.count(".") > 1 or b.count(".") > 1:
    	print("INVALID")
    	print("")
    elif float(b) == 0:
    	print("KILL YOURSELF")
    	print("")
    else:
    	division = float(a) / float(b)
    	print(division)
    	print("")
while question == "square root" or question == "5":
	a = input("What number: ").strip().lower()
	a = a.replace(" ", "")
	if str(a).isalpha() == True:
		print("INVALID")
		print("")
	elif a.count("\\") >= 1 or a.count("[") >= 1 or a.count("]") >= 1 or a.count("(") >= 1 or a.count(")") >= 1 or a.count("{") or a.count("}") >= 1:
		print("INVALID")
		print("")
	elif str(a) == "":
		print("INVALID")
		print("")
	elif re.search(special_chars, a):
		print("INVALID")
		print("")
	elif str(a) == ".":
		print("INVALID")
		print("")
	elif a.count(".") > 1:
		print("INVALID")
		print("")
	elif re.search(letters, a):
		print("INVALID")
		print("")
	elif float(a) == 0:
		print("KILL YOURSELF")
		print("")
	else:
		a = float(a)
		squareroot = math.sqrt(a)
		print(squareroot)
		print("")