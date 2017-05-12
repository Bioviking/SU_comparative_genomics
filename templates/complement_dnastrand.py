#############################################################

#Write a function that gets the complement of a DNA sequence.

def complement(seq):
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')
    seq = seq.replace('A', 't')
    seq = seq.replace('T', 'a')
    return seq.upper()
    
print(complement('ATCTCGTGCA'))


def write_complement(input_file_name, output_file_name):
    f_in = open(input_file_name, 'r')
    f_out = open(output_file_name, 'w+')
    #line_list = []  
    for line in f_in:
        line = line.strip()
        #print(line) 
        if line[0] == '>':
            line = line[1:] + ' complement \n'
            #line_list.append(line)
            f_out.write(line)
            #print(line)
        else:
            line = line.strip()  
            line = line.replace('G', 'c')
            line = line.replace('C', 'g')
            line = line.replace('A', 't')
            line = line.replace('T', 'a')                   
            f_out.write(line.upper() + '\n') 
            #print(line.upper(),'\n')
    f_in.close()
    f_out.close()
    return output_file_name
print(write_complement('dna_sequences', 'output_dna_sequences'))
    
