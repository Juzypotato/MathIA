
# Constants, these are for the encryption
e = 83
d = 59
n = 323


def encrypt():
	m = input("Please enter a message (number plz)\nInput: ")
	c = pow(int(m), e) % n
	return c


def decrypt():
	c = input("Please enter a message (number plz)\nInput: ")
	m = pow(int(c), d) % n
	return m


def main():
	mode = input("Would you like to run the application for\n(1)Encryption\n(2)Decryption\n(3)GUI (Not ready)\nInput: ")
	try:
		if int(mode) == 1:
			print("Your encrypted message is", encrypt(), "\n")
			if input("Return to main? (y) (n)\n") == "y":
				main()
			else:
				return 0
		elif int(mode) == 2:
			print("The decrypted message is", decrypt(), "\n")
			if input("Return to main? (y) (n)\n") == "y":
				main()
			else:
				return 0
		else:
			print("You did something wrong :p")
			if input("Return to main? (y) (n)\n") == "y":
				main()
			else:
				return 0
	except ValueError:
		print("Shit dude, that was wrong")
		if input("Return to main? (y) (n)\n") == "y":
			main()
		else:
			return 0


if __name__ == '__main__':
	main()
