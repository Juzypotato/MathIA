import math

def divisor(num):
    # Function determines and returns the divisors of any given number
    list_divisor = []
    for counter in range(2, num):
        if num % counter == 0:
            list_divisor.append(counter)
    return list_divisor


def findE(Carf):
    e = int(Carf * 0.5)
    while True:
        if math.gcd(e, Carf) == 1:
            return e
        else:
            e += 1


def findD(e, Car):
    d = int(Car * 0.5)
    while True:
        if (d*e) % Car == 1:
            return d
        else:
            d += 1



def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def isPrimef(num):
    # Funtion returns whether number is prime or not
    output = True
    if (num < 2):
        output = False
    else:
        counter = 2
        while (counter < num):
            if (num % counter == 0):
                output = False
                break
            else:
                counter += 1
    return output


def main():
    number = int(input("What number do you want to know if is prime? "))
    primeOrNot = isPrime(number)
    if (primeOrNot is False):
        print(number, " is not prime.")
        print(divisor(number), "Are the divisors of", number)
    elif (primeOrNot is True):
        print(number, " is prime.")


if __name__ == '__main__':
    main()
