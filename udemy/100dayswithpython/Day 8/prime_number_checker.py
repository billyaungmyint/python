def prime_checker(number):
    isprime = True
    for n in range(2,number):
        if number % n == 0:
            isprime = False
        else:
            isprime = True
    
    if isprime == False :
        print("The number is not a prime number.")
    else:
        print("The number is a prime number.")

n = int(input("Check this number : "))
prime_checker(n)