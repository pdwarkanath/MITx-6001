def genPrimes():
    primes = []
    x = 2
    
    while True:
        isPrime = True
        
        for p in primes:
            if (x % p) != 0:
                continue
            else:
                isPrime = False
                break
        if isPrime == True:
            primes.append(x)
            yield x
        x +=1
