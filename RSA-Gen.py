import isPrime


def error():
	if input("You typed something wrong, try again? (y)(n)\n") == "y":
		print("\n")
		main()
	else:
		return "Error"


def main():
	try:
		p, q = input("Please enter large integer primes for p and q separated by ','\nInput: ").split(",")
		p, q = int(p), int(q)
		n = p*q
		print(n)
		Carf = lcm(p-1, q-1)
		print(Carf)
		e = findE(Carf)
		print(e)
		d = findD(e, Carf)
		print("\nn =", n, "\ne =", e, "\nd =", d)
	except ValueError:
		error()


if __name__ == '__main__':
	main()
