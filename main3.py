def is_prime(x):
    """
    determina daca un numar intreg e prim
    param. x - un numar intreg
    return - True daca x e prim, False in caz contrar
    """
    if x < 2: return False
    for i in range(2, x//2+1):
        if x % i == 0: return False
    return True
    

def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(2) == True
    assert is_prime(997) == True


test_is_prime()




def is_palindrome(n) -> bool:
    """
    Determină dacă un număr dat este palindrom
    param. n - numarul dat
    return - True daca n este palindrom, False in caz contrar
     """
    copie_n = n
    oglindit_n = 0
    while copie_n > 0:
        oglindit_n = 10 * oglindit_n + copie_n % 10
        copie_n = copie_n // 10
    if n == oglindit_n: return True
    return False


def test_is_palindrome():
    assert is_palindrome(0) == True
    assert is_palindrome(6498946) == True
    assert is_palindrome(481579) == False


test_is_palindrome()



'''
  Aratati daca un numar este superprim sau nu
'''
def is_superprime(n):

    clona = n
    if n < 2:
        return False
    elif n % 2 == 0:
        return False
    else:
        while clona != 0:
            for i in range(3, clona//2):
                if n % i == 0:
                    return False
            clona = clona//10
    return True


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(2689) is False
    assert is_superprime(37) is True
    assert is_superprime(8234) is False
    assert is_superprime(25) is True


test is_superprime()


def input_isprime():
    x = int(input("Introduceti numarul "))
    print(isprime(x))

def input_is_palindrome():
    x = int(input("Introduceti numarul "))
    print(is_palindrome(x))

def input_is_superprime():
    x= int(input("Introduceti numarul"))
    print(is_superprime(x))


def main():
    while True:
        print("""
        Alegeti functia:
        1) is_prime
        2) is_palindrome
        3) is_superprime
        4) stop program
        """)
        option = int(input("Optiune: "))
        if option == 1: input_is_prime()
        elif option == 2: input_is_palindrome()
        elif option == 3: input_is_superprime()
        elif option == 4: break
        else: print("Optiune invalida")


main()