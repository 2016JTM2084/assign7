###### this is the first .py file ###########

####### write your code here ##########
import sys
d={}
a=list(sys.argv)
l=range(1,len(a))
for i in range(1,len(a)):
	c=0
	for j in range(1,len(a)):
		if a[i]==a[j]:
			c=c+1
	l[i-1]=c	
	d.update({a[i]:c})

print d
