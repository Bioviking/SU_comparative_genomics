# (*) Make a function dist(a, b) that takes two DNA sequences of the same length and returns the Hamming distance between them, i.e., the number of symbols at the same position that differ. For example, dist('GGGAT', 'GGCCT') = 2, because GA -> CC and everything else remains the same.

def dist(a, b):
    '''Compute the Hamming distance between A and B
    Example: dist(â€™GGGATâ€™, â€™GGCCTâ€™) = 2
    '''
    total = 0 
    for i in range(0, len(a)):
        if a[i] != b[i]: 
            total += 1
    return total

#print('Hamming:')
#print(dist('GGGAT', 'GGCCT'))
