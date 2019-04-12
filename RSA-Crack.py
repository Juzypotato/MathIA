import time
import decimal


def crack(n, i):
    while True:
        a = decimal.Decimal(n/i)
        if a == int(a):
            return a
        else:
            i += 1


def main():
    n = decimal.Decimal(input("What is the product of the primes? : "))
    #n = decimal.Decimal(112981889*112980389)
    mode = input("How many decimal points should be calculated?\n1. 16\n2. 128\n3. Very large\nMode: ")
    if mode == "1":
        decimal.getcontext().prec = 16
    elif mode == "2":
        decimal.getcontext().prec = 128
    elif mode == "3":
        decimal.getcontext().prec = 512000
    else:
        print("You didn't choose an option correctly, try again")
        main()

    print("Processing...")
    start_time = time.time()
    q = crack(n, 2)
    p = crack(n, q)
    print("The factors of n are\np =", p, "\nq =", q)
    print("--- %ss ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
