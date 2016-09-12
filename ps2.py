###### this is the second .py file ###########

####### write your code here ##########

import random,math						        # importing the packages for using the function defined within them
a=input("enter the number of users in the locality \n") 		# taking the no. of users from the user
c=0
for i in range(a): 							# generating the location of the users 
	(x,y)=(random.random()*2- 1, random.random()*2-1)
	d=math.sqrt(x*x+y*y)    					# calculating the distance of each user from origin
	if d<=1:   							#if distance is less than equal to unity they lie within range of tower
		c=c+1      						# incrementing the no of user in range
p=(float(c)/float(a))*100						# calculating the percentage of users in range
print p
