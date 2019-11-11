# This code calculates the amount, given the principal, rate of interest, and number of years:

# This does not calculate the yearly additions to the principal amount !!!

# The defaults are rate of int = 6%, time is 1 year, and principal = 100 rupees
# The formula used is https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php

r  = 0.06
t  = 1
nt = 12 *t
p= 100

x= r/12
x= x+1;
x = x**nt
a= x*p
i=1
print ("Starting the principal with ", p);
print(" At the end of year %d, r= %0.2f Percent,  Amount = % 0.2f"% (i,r*100, a)) 
for i in range (1,10):
	#print (i)
	p = a;
	a = p*x
	
	print(" At the end of year %d, r= %0.2f Percent,  Amount = % 0.2f"% (i+1,r*100, a)) 
