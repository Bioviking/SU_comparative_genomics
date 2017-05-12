#######################################################
#(*) Define a function longest_line(file_name) that takes as an input a file name and returns the length of the longest line in the file.
def longest_line(file_name):
    f = open(file_name)
    lengths = []
    for line in f:
        line = line.strip()
        lengths.append(len(line))
    return sorted(lengths)[-1]

#print(longest_line('test_longest_line.dat'))
