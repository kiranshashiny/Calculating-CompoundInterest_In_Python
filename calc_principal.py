#This code does the reverse, calculates the principal every year, given the amount 
# to be repaid after 10 years.

# This code goes with calc_amount.py
# the 181.99 was derived from 'if the user deposited 100 rupees for 1years.
# You will notice that after 10 years, the amount is back to 100 rupees.

r  = 0.06
t  = 1
nt = 12 *t
a= 181.99


x= r/12
x= x+1;
x = x**nt

i=1
print(" Starting Amount = % 0.2f" % ( a )) 

for i in range (0,10):
	
	p = a/x;
	print(" At the end of year %d, r= %0.2f Percent,  Amount = % 0.2f"% (i+1,r*100, p)) 
	a=p
