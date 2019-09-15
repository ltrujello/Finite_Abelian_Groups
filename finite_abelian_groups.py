from itertools import product
#code to get first 100,000 primes
hun_tho_primes = []
hun_primes = open('100000_primes.txt', 'r').read()
hun_primes = hun_primes.split('\n') 
for i in range(8, 22231):                   #list starts at line =  8. List is from U of Texas.
    hun_tho_primes += hun_primes[i].split() #populates list with values.
for i in range(len(hun_tho_primes)): 
    hun_tho_primes[i] = int(hun_tho_primes[i]) #converts the values from str to int

def primefac(ord):
    "Input is an integer, and the output is an ordered mulitset of primes factors "
    "of ord."
    L = []
    I = [i for i in hun_tho_primes if i <= (ord)]
    for i in I:
        if ord == 1:    
            break
        while ord % i == 0:
            L.append(i)
            ord /= i
    return L

def power_count(i, L): #helper function
    "determines number of times an element appears in a list. "
    "The order of the elements in which they appear does not matter."
    count = 0
    if i not in L:
        return i, print(" is not in the list "), L #checks if error happened in all_prods
    else:
        for k in L:
            if k == i:
                count += 1
    return count

def prime_pows(L):
    "Given a multiset of primes L, the output is a list of 2-tuples, where for each tuple, the first" 
    "coordinate is a prime, and the second coordinate is the primes' power."
    primes, powers = [], []
    if L == []:                 #checks if error happened in prime_fac
        return("There are no prime factors! Something is wrong in primefac.")
    i = 0
    while i in range(len(L)):
        j = L[i]
        pow = power_count(j, L) #This is never zero; previous step guarantees that. 
        primes.append(j)        #Hence, we'll never have an infinite while loop based on the last step. 
        powers.append(pow)
        i += pow                #Pow is at least 1. 
    prime_powers = list(zip(primes, powers)) #contains tuples. first entry is the prime, second is the power. 
    return prime_powers

def decompose_ahead(prime_pows):
    "The input is the list of tuples, where the first coordinate is a prime, "
    "the second coordinate is the power. The function returns a list of list, "
    "where each sublist  contains all products of a prime to its power."
    "This is achieved by recurison."
    if len(prime_pows) == 0:
        return []
    prime = prime_pows[0][0] #the prime
    power = prime_pows[0][1] #the prime's power
    prods = []
    for i in range(1, prime_pows[0][1] + 1):
        prods += [[prime**i] + (power - i)*[prime]] #one at a time, raises the prime to its power
    return [prods] + decompose_ahead(prime_pows[1:])#moves on to the next prime

def produce_factors(all_factors):
    "The input is the list of lists containing primes to their power, while" 
    "the output is the set of all factorizations of the desired integer."
    final_list = []
    sorted_prods = []
    K = list(all_factors) #forces it to be of type list
    products = list(product(*K)) #takes the cartesian product
    for prod in products: #rest of code just neatly organizes the products 
        final_list = []
        for elem in prod:
            final_list += elem 
        sorted_prods += [final_list]
    return sorted_prods

def all_factorizations(theint):
    return produce_factors(decompose_ahead(prime_pows(primefac(theint))))