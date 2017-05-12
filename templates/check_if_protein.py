###############################################
#(*) Given a string of characters, write a function is_protein(seq) that returns True if it is a valid protein sequence, else False. We consider a a valid protein something that contains only valid aminoacids: ACDEFGHIKLMNPQRSTVWY in capital letters.
def is_protein(seq):
    for i in seq:   
        if i not in 'ACDEFGHIKLMNPQRSTVWY':
            return False    
    return True 
#print(is_protein('ACDEFGHIKLMNPQRSTVWY'))
