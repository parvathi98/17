# no is palindrome
import sys
t = int(input('enter t :'))
a = str(t)
if  a == a[::-1] :
	print(‘yes’)
else :            
	print(‘no’)
