import math
import time

print('Karatsuba multiplication in Python')
x=raw_input("first_number=")
y=raw_input("second_number=")
print('------------------------')
x=int(x)
y=int(y)

def karatsuba(x,y):

	x=str(x)
	y=str(y)

	len_x=len(x)
	len_y=len(y)

	if(int(len_x)==1 or int(len_y)==1):    
		return int(x)*int(y)
	else:

		B=10
		exp1=int(math.ceil(len_x/2.0))
		exp2=int(math.ceil(len_y/2.0))
		if(exp1<exp2):
			exp=exp1
		else:
			exp=exp2
			m1=len_x-exp
			m2=len_y-exp
			a=karatsuba(int(x[0:m1]),int(y[0:m2]))
			c=karatsuba(int(x[m1:len_x]),int(y[m2:len_y]))
			b=karatsuba(int(x[0:m1])+int(x[m1:len_x]),int(y[0:m2])+int(y[m2:len_y]))-a-c
			results=a*math.pow(10,2*exp) + b*math.pow(10,exp) + c
			return int(results)

			start_time=time.time()
			ctrl = x*y
			tpt=time.time() - start_time
			print x,'*',y,'=',ctrl
			print("--- %s seconds ---" % tpt)

			start_time=time.time()
			output=karatsuba(x,y)
			tpt=time.time() - start_time
			print 'karatsuba(',x,',',y,')=',output
			print("--- %s seconds ---" % tpt)

karatsuba(x,y)