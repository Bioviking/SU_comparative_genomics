#3.Use the previous parser to load a file and make a dictionary mapping ids to GC content.



def map_id(filename):
    g_dict = parse_fasta(filename)
    count = 0
    total = 0
    for key, value in g_dict:
        #line = line.strip()
        for i in range(len(value)):
                char = value[i]
                if char == 'G' or char == 'C':
                    count = count + 1
                    total = count / len(value)     
                return total
                print(total)
    return g_dict

print(map_id('example.fasta'))

parse_fasta('example.fasta')
def compute_gc(sequence):
    count = 0
    total = 0
    for i in range(len(sequence)):
        char = sequence[i]
        if char == 'G' or char == 'C':
            count = count + 1
    total = count / len(sequence)     
    return total

