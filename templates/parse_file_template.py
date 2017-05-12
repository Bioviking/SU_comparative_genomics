###############################################################################
#11.Write a parser for a Multiple Sequence Alignment in Jones/ALN format. In this format, each line contains one protein sequence. 

##################################################################3
#12. (*) Same as above, but now you should parse a FASTA file: each sequence has a header in the previous line starting with the charater “>”. Call this function parse_fasta and return the results as a list. 
############3List####################################
def parse_fasta(file_name):
    f = open(file_name, 'r')
    line_list = [] 
    header_list = []  
    for line in f:
        line = line.strip() 
        if line[0] == '>':
            line = line.strip(' ')
            line = line[1:]
            header_list.append(line)
        else:
            line_list.append(line)
    f.close()
    return line_list #['PEPTIDE', 'PEPT-KE']
    

print(parse_fasta('number12.fasta'))

########################Dictionary#######################
def parse_fasta(filename):
    f = open(filename,'r')
    
    g_dict = dict()
    for line in f:
        line = line.strip()
        if line[0] == '>':
            line = line[1:]
            temp_id = line
        else:
            g_dict[temp_id] = line
    return g_dict

#parse_fasta('example.fasta')

