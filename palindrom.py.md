#modificare mod de rezolvare problema
#aratati ca un numar este palindrom sau nu
def is_palindrome(n):
	numar=n
	rasturnat=0
	while n!=0:
		ultima cifra=n%10
		rasturnat=rasturnat*10+ultima cifra
		n=n//10
	if rasturnat==numar:
		return True
	else
		return False
def test_is_palindrome():
	assert is_palindrome(121) is True	
	assert is_palindrome(233) is False
	assert is_palindrome(22) is True
	assert is_palindrome(150) is False
	assert is_palindrome(334) is False


#Aratati daca un numar este prim sau nu 
def prime(n):
	if n>1:
		for i in range(2,n):
			if(n%i)==0:
				print(n,"nu este prim")
			else:
				print(n,"n este prim")
n= int(input("Dati un numar:"))
prime(n)
def test_is_prime():
	assert is_prime(21) is False
	assert is_prime(2) is True
	assert is_prime(13) is True
	assert is_prime(26) is False
	assert is_prime(156) is False

#Aratati daca un numar este sau nu antipalindrom
def is_antipalindrome(n):

    clona=n
    rasturnat=0
    nrcifre=0

    while clona:

        rasturnat=rasturnat*10+clona%10
        clona=clona//10
        nrcifre=nrcifre+1

    if nrcifre % 2 == 1:
        ok=0
    else: ok=1

    while rasturnat:
        if rasturnat%10 == n%10:
            ok=ok+1
        if ok==2:
            return False
        rasturnat=rasturnat//10
        n=n//10
  return True

def test_is_antipalindrome():

    assert is_antipalindrome(34256) == True
    assert is_antipalindrome(121) == False
    assert is_antipalindrome(333) == False
    assert is_antipalindrome(1234) == True
    assert is_antipalindrome(321678) == True
    assert is_antipalindrome(55555) == False
    assert is_antipalindrome(22)==False

#Aratati daca un numar este superprim sau nu 
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
