item --> allow to read only one item
items --> upload allow item and iterate over them


#=======================================#
# Single Sequences
#=======================================#

# -----------------------------			
# (1) KNOWN number of elements.
# A sequence consisting of a number N, followed by N elements
'''
10   hello bye you me one this three now then just
'''
n = int(item())  # read number of elements --> n (10)
for _ in range(n) : # repeat n times
	x = item() # read next element 
	# do something with x
	
	
# -----------------------------				
# (2) UNKNOWN number of elements, no end mark.

'''
hello bye you me one this three now then just
'''
for x in items() :  # for each element in the input
	# do something with x


# -----------------------------				
# (3) UNKNOWN number of elements, with end mark.
'''
hello bye you me one this three now then just STOP
'''
x = item() # read first element
while x != 'STOP' :  # as long as the last read element is not the special one
  # do something with x 
  x = item() # read next element (and repeat to see if it is STOP or not)

  
#===========================================#
# Several sequences (sequence of sequences)
#===========================================#


# -----------------------------			
# KNOWN number of sequences, KNOWN number of elements.

# In this case, we use the schema (1) above twice: one for the sequences
# (outer for loop), and another for the elements in each sequence (inner loop)

'''
3
10  hello bye you me one this three now then just
2   sun moon
4   one six my foot
'''
n = int(item())    # number of sequences
for _ in range(n) :  # repeat n times (one per sequence)

	m = int(item()) # number of elements in current sequence
	for _ in range(m) : # repeat m times (one per element in this sequence)
		x = item()  # get current element in the sequence
		# do something with x

	# do something about this sequence, if needed,
	# before moving to the next one


# -----------------------------			
# KNOWN number of sequences, UNKNOWN number of elements, with mark.
'''
3
hello bye you me one this three now then just STOP
sun moon STOP
one six my foot STOP
'''
n = int(item())    # number of sequences
for _ in range(n) :  # repeat n times (one per sequence)

	x = item()   # get first element in current sequence
	while x != 'STOP' :
		# do something with x
		x = item()  # get next element
  
	# do something about this sequence, if needed,
	# before moving to the next one


# -----------------------------			
# UNKNOWN number of sequences, KNOWN number of elements in each.
'''
10 hello bye you me one this three now then just
2 sun moon
4 one six my foot
'''
for n in items() :  # get an element (it will be the number of elements
                    # in the upcoming sequence, if any)
	n = int(n)	
	for _ in range(n) : # repeat n times (one for each element in the sequence)
		x = item()  # get the element
		# do something with x
		# before moving to the next one


# -----------------------------			
# UNKNOWN number of sequences, UNKNOWN number of elements, with mark.
'''
hello bye you me one this three now then just STOP
sun moon STOP
one six my foot STOP
'''
for x in items() :  # get an element (it will be the first 
                    # element in a sequence, if any)

	while x != 'STOP' :  # as log as the last read element is not the end mark
		# do something with x
		x = item() # get next element (and loop to see whether it is STOP)
  
	# do something about this sequence, if needed,
	# before moving to the next one

  
