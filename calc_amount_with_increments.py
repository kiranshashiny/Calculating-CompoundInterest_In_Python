# This code calculates the amount, given the principal, rate of interest, and number of years:

# This does not calculate the yearly additions to the principal amount !!!

# The defaults are rate of int = 6%, time is 1 year, and principal = 100 rupees
# The formula used is https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php

r  = 0.06
t  = 1
nt = 12 *t
p= 100
yearly_increments=100

x= r/12
x= x+1;
x = x**nt
a= x*p
i=1
print ("Starting the principal with ", p);
print(" At the end of year %d, r= %0.2f Percent,  Started with %d, Amount = % 0.2f"% (i,r*100,p, a)) 
for i in range (1,10):
	#print (i)
	old_a =a;
	p = a;
	p = p+yearly_increments;
	a = p*x
	
	print(" At the end of year %d, r= %0.2f Percent,  Started with (%0.2f + %d) = %d, Amount = % 0.2f"% (i+1,r*100, old_a, yearly_increments, old_a+yearly_increments, a)) 
