###### this is the third .py file ###########

####### write your code here ##########

state={"UTTARAKHAND":'000',"GOA":'001',"NEW DELHI":'010',"PUNJAB":'011'}
city={"ROORKEE":'111',"NEW DELHI":'110',"PANAJI":'101',"AMRITSAR":'100'}
district={"IIT ROORKEE":'000',"NIT GOA":'001',"IIT DELHI":'010',"NIT JALANDHAR":'011'}
print "1.add 2.modify 3.delete 4.query"
a=input("enter the operation you want to perform")
if a==1:
	s=raw_input("enter the state name you want to add")
	m=raw_input("enter the code name you want to add for state")
	state.update({s:m})
	c=raw_input("enter the city name you want to add")
	n=raw_input("enter the code name you want to add for city")
	city.update({c:n})
	d=raw_input("enter the district name you want to add")
	q=raw_input("enter the code name you want to add for district")
	district.update({d:q})
	print "added successfully"	
if a==3:	
	b=raw_input("enter the state want to delete\n")
	if b in state.keys():	
		del state[b]
	else :
		print "not a valid key"
	b=raw_input("enter the city want to delete\n")
	if b in city.keys():	
		del city[b]
	else :
		print "not a valid key" 
	b=raw_input("enter the district want to delete\n")
	if b in district.keys():	
		del district[b]
	else :
		print "not a valid key"
	print "deleted successfully"
if a==2:
	t1=raw_input("enter the state whose code you want to modify\n")
	t11=raw_input("enter the new code\n")
	if t1 in state.keys():
		state.update({t1:t11})
	else :
		print 'not a valid state'
	t2=raw_input("enter the district whose code you want to modify\n")
	t21=raw_input("enter the new code\n")
	if t2 in district.keys():
		district.update({t2:t21})
	else :
		print 'not a valid district'
	t3=raw_input("enter the city whose code you want to modify\n")
	t31=raw_input("enter the new code\n")
	if t3 in city.keys():
		city.update({t3:t31})
	else :
		print 'not a valid city'
	print "updated successfully"
else :
	l1=raw_input("enter the customer name\n")
	l2=raw_input("enter the customer district\n")
	l3=raw_input("enter the customer city\n")
	l4=raw_input("enter the customer state\n")
	print "Collection Center No."
	if l1 in state.keys():
		print "CC_NO = %s" % state.get(l4, "None")
	if l1 in district.keys():
		print district.get(l2, "None")
	if l1 in city.keys():
		print city.get(l3, "None")
	
	

