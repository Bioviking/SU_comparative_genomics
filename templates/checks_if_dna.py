#########################################################

#Given a string of characters, write a function that returns True if it is a valid DNA sequence, and False if it isn’t. DNA contains uniquely GATC.

def is_dna(seq):
    flag = True
    for i in seq: #range(0, len(seq)):    
        if i == 'G' or i =='A' or i =='C' or i =='T':         
            continue
        else:
            flag = False
        print(i, flag)
    return flag 
print(is_dna('ATCTCGTRCA'))
