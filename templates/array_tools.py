##########################################################################
import numpy as np

def reverse_array(input_array):
  rev = input_array[::-1]  # Fix this!
  return rev

#print(reverse_array([1, 2, 3]))


#############################################################

import numpy as np
def sort_array(input_array):
    sorted_array = np.array(input_array)
    #sorted_array = np.ndarray.sort(in_array)
    np.ndarray.sort(sorted_array)
    print('Original input:', input_array)
    return sorted_array
#print('Sorted array', sort_array([9, 2, 3, 6, 5, 9, 7, 4, 1, 8]))
