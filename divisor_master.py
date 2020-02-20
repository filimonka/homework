# Light

def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def all_divisors(n):
    div_list = [1, n]
    for i in range(2, n):
        if n % i == 0:
            div_list.append(i)
    return div_list


def biggest_prime_divisor(n):
    prime_div_list = []
    for el in all_divisors(n):
        if prime(el) == True and n % el == 0:
            prime_list.append(el)
    prime_list.sort()
    return prime_div_list[-1]



# PRO
def prime_list(s,st):
    prime_list = []
    for i in range(s, st):
        if prime(i) == True:
            prime_list.append(i)
    return prime_list


def can_dec_dev(n):
    div = {}
    result = []
    primes = prime_list(2, n)
    i = 0
    a = 0
    while i <= len(primes):
        while n != 1:
            if n %  primes[i] == 0:
                if primes[i] not in div:
                    div[primes[i]] = 1
                else:
                    div[primes[i]] += 1
                n //= primes[i]
            else:
                i += 1
        break
    for values in div.items():
        if values[1] > 1:
            result.append(str(values[0]) + '^' + str(values[1]))
        else:
            result.append(values[0])
    return  result


def biggest_div(n):
    a = all_divisors(n)
    a.sort(reverse=True)
    return  a[1]
    # если имеется в виду само число как наибольший делитель, то тогда 0 элемент вернуть
