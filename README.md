#Determinati daca un numar este palindrom sau nu
def is_palindrome(n):
	x= int(n)
	while x:
		y=x%10+y*10
                x=x/10
	if y==n:
		print("Da")
	else:
		print("Nu")
z= int (input("Dati un numar:")
is_palindrome(z)