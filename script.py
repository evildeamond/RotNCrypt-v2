import os
import string

def make_rot_n(n):
 lc = string.ascii_lowercase
 uc = string.ascii_uppercase
 trans = string.maketrans(lc + uc,
						  lc[n:] + lc[:n] + uc[n:] + uc[:n])
 return lambda s: string.translate(s, trans)

rot1 = make_rot_n(1)
rot2 = make_rot_n(2)
rot3 = make_rot_n(3)
rot4 = make_rot_n(4)
rot5 = make_rot_n(5)
rot6 = make_rot_n(6)
rot7 = make_rot_n(7)
rot8 = make_rot_n(8)
rot9 = make_rot_n(9)
rot10 = make_rot_n(10)
rot11 = make_rot_n(11)
rot12 = make_rot_n(12)
rot13 = make_rot_n(13)
rot14 = make_rot_n(14)
rot15 = make_rot_n(15)
rot16 = make_rot_n(16)
rot17 = make_rot_n(17)
rot18 = make_rot_n(18)
rot19 = make_rot_n(19)
rot20 = make_rot_n(20)
rot21 = make_rot_n(21)
rot22 = make_rot_n(22)
rot23 = make_rot_n(23)
rot24 = make_rot_n(24)
rot25 = make_rot_n(25)

print ('''    ____  ____  ______      ______          
   / __ \/ __ \/_  __/___  / ____/______  ______  / /_
  / /_/ / / / / / / / __ \/ /   / ___/ / / / __ \/ __/
 / _, _/ /_/ / / / / / / / /___/ /  / /_/ / /_/ / /_  
/_/ |_|\____/ /_/ /_/ /_/\____/_/   \__, / .___/\__/  
								   /____/_/           
								   ''')
print ('''          Version 2.0

	''')
menu = True
while menu:
	menu = raw_input ("""
1.ENCRYPT Using ROT
2.DECRYPT using ROT

Press The Enter Key to Exit this Script


What would you like to do?
""")
	if menu =="1":
		plain = raw_input("Type Plain-Text to be Encrypted: ")
		rotn = raw_input("How many places to you wish to move by?")
		if rotn == "1":
			print rot1(plain)
		elif rotn == "2":
			print rot2(plain)
		elif rotn == "3":
			print rot3(plain)
		elif rotn == "4":
			print rot4(plain)
		elif rotn == "5":
			print rot5(plain)
		elif rotn == "6":
			print rot6(plain)
		elif rotn == "7":
			print rot7(plain)
		elif rotn == "8":
			print rot8(plain)
		elif rotn == "9":
			print rot9(plain)
		elif rotn == "10":
			print rot10(plain)
		elif rotn == "11":
			print rot11(plain)
		elif rotn == "12":
			print rot12(plain)
		elif rotn == "13":
			print rot13(plain)
		elif rotn == "14":
			print rot14(plain)
		elif rotn == "15":
			print rot15(plain)
		elif rotn == "16":
			print rot16(plain)
		elif rotn == "17":
			print rot17(plain)
		elif rotn == "18":
			print rot18(plain)
		elif rotn == "19":
			print rot19(plain)
		elif rotn == "20":
			print rot20(plain)
		elif rotn == "21":
			print rot21(plain)
		elif rotn == "22":
			print rot22(plain)
		elif rotn == "23":
			print rot23(plain)
		elif rotn == "24":
			print rot24(plain)
		elif rotn == "25":
			print rot25(plain)
		raw_input()
		os.system('cls' if os.name == 'nt' else 'clear')
	elif menu =="2":
		encrypted = raw_input("Enter Encrypted ROT Phrase: ")
		print rot1(encrypted)
		print rot2(encrypted)
		print rot3(encrypted)
		print rot4(encrypted)
		print rot5(encrypted)
		print rot6(encrypted)
		print rot7(encrypted)
		print rot8(encrypted)
		print rot9(encrypted)
		print rot10(encrypted)
		print rot11(encrypted)
		print rot12(encrypted)
		print rot13(encrypted)
		print rot14(encrypted)
		print rot15(encrypted)
		print rot16(encrypted)
		print rot17(encrypted)
		print rot18(encrypted)
		print rot19(encrypted)
		print rot20(encrypted)
		print rot21(encrypted)
		print rot22(encrypted)
		print rot23(encrypted)
		print rot24(encrypted)
		print rot25(encrypted)
		raw_input()
		os.system('cls' if os.name == 'nt' else 'clear')
	elif menu !="":
		print("\n Not Valid Choice Try again")
