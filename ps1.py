# Python program to count words in a given string
out = 0
IN = 1
 
# Returns number of words in string
def countWords(string):
    state = out
    wc = 0
 

    for i in xrange(len(string)):
 
        # If next character is a separator, set the
        # state as OUT
        if (string[i] == ' ' or string[i] == '\n' or
            string[i] == '\t'):
            state = out
 
        # If next character is not a word separator
        # and state is OUT, then set the state as
        # IN and increment word count
        elif state == out:
            state = IN
            wc+=1
 
    # Return the number of words
    return wc
 
# Driver program
string =raw_input("enter the string\n")
print "No. of words: " + str(countWords(string))
list1 =string.split()
wordfreq =[]
for w in list1 :
	wordfreq.append(list1.count(w))

print("Frequencies\n" + str(wordfreq) + "\n")
print "Max value element : ", max(wordfreq)
print "Max value element : ", max(list1)

def toString(List):
    return ''.join(List)
 
# 1. String

# 2. Starting index of the string

# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print toString(a)
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]
stri=max(list1)
n = len(stri)
a = list(stri)

permute(a,0,n-1)
