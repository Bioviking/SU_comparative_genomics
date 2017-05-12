########################################################################################3
# 1. (*) Create a function that takes a string of nucleotids as input and returns its GC content as a number between 0 and 1. Call it compute_gc.
def compute_gc(sequence):
    count = 0
    total = 0
    for i in range(len(sequence)):
        char = sequence[i]
        if char == 'G' or char == 'C':
            count += 1
    total = count / len(sequence)     
    return total           
	

print()
print()
print('GC:')
print(compute_gc('GGGATACCC'))
print(compute_gc('AAACGTTGTGTTCCAAGGCTTGATATAGTCACGAT'))

#print()
#print()
