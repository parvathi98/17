# no is prime
import sys
n = int(input())
if n==1 :
	print(‘No’)
elif n==2 or n==3 :
	print(‘Yes’)
else :
    for i in range(2,n) :
	if n%i == 0 :
	    print(‘No’)
	    sys.exit()
    else :
	print(‘Yes’)
