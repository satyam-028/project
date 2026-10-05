def prime_numebr(x):
    # num = int(input("enter a number : "))
    if x == 1:
        print(f"this not a prime {x}" )
    elif x%2==0:
        print(f"this number is not prime : {x} ")
    else:
        print(f"The number is prime : {x}")
var = prime_numebr(233)