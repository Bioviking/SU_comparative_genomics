'''
Calculating the distance matrix

To calculate the distance matrix between the items stored in the record, use

>>> matrix = record.distancematrix()

where the following arguments are defined:

    transpose (default: 0)
    Determines if the distances between the rows of data are to be calculated (transpose==0), or between the columns of data (transpose==1).
    dist (default: 'e', Euclidean distance)
    Defines the distance function to be used (see 15.1). 

This function returns the distance matrix as a list of rows, where the number of columns of each row is equal to the row number (see section 15.1).
'''
