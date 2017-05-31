import gzip
import os

file_1 = "2211/Desktop/hello.gz"
file_path = os.path() + file_1

with open(file_path, 'r') as f:
    
    file_content = f.read()
    print(file_content)
    #for line in file_content:
     #   print(line[0])
        
        
        
        #272561 Chlamydia trachomatis
        #316385 Escherichia coli str. K-12
        #243231 Geobacter sulfurreducens PCA
        #251221 Gloeobacter violaceus
        #4932 Saccharomyces cerevisiae
