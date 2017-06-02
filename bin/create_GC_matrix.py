############## Distance Matrix GC content #############
import math

GC1 = 41.3
GC2 = 50.6
GC3 = 60.2
GC4 = 62
GC5 = 39

D11 = math.sqrt((GC1-GC1)**2)
D12 = math.sqrt((GC1-GC2)**2)
D13 = math.sqrt((GC1-GC3)**2)
D14 = math.sqrt((GC1-GC4)**2)
D15 = math.sqrt((GC1-GC5)**2)

D21 = math.sqrt((GC2-GC1)**2)
D22 = math.sqrt((GC2-GC2)**2)
D23 = math.sqrt((GC2-GC3)**2)
D24 = math.sqrt((GC2-GC4)**2)
D25 = math.sqrt((GC2-GC5)**2)

D31 = math.sqrt((GC3-GC1)**2)
D32 = math.sqrt((GC3-GC2)**2)
D33 = math.sqrt((GC3-GC3)**2)
D34 = math.sqrt((GC3-GC4)**2)
D35 = math.sqrt((GC3-GC5)**2)

D41 = math.sqrt((GC4-GC1)**2)
D42 = math.sqrt((GC4-GC2)**2)
D43 = math.sqrt((GC4-GC3)**2)
D44 = math.sqrt((GC4-GC4)**2)
D45 = math.sqrt((GC4-GC5)**2)

D51 = math.sqrt((GC5-GC1)**2)
D52 = math.sqrt((GC5-GC2)**2)
D53 = math.sqrt((GC5-GC3)**2)
D54 = math.sqrt((GC5-GC4)**2)
D55 = math.sqrt((GC5-GC5)**2)

print('Distance Matrix Value 1-1', D11)
print('Distance Matrix Value 1-2', D12)
print('Distance Matrix Value 1-3', D13)
print('Distance Matrix Value 1-4', D14)
print('Distance Matrix Value 1-5', D15)

print('Distance Matrix Value 2-1', D21)
print('Distance Matrix Value 2-2', D22)
print('Distance Matrix Value 2-3', D23)
print('Distance Matrix Value 2-4', D24)
print('Distance Matrix Value 2-5', D25)

print('Distance Matrix Value 3-1', D31)
print('Distance Matrix Value 3-2', D32)
print('Distance Matrix Value 3-3', D33)
print('Distance Matrix Value 3-4', D34)
print('Distance Matrix Value 3-5', D35)

print('Distance Matrix Value 4-1', D41)
print('Distance Matrix Value 4-2', D42)
print('Distance Matrix Value 4-3', D43)
print('Distance Matrix Value 4-4', D44)
print('Distance Matrix Value 4-5', D45)

print('Distance Matrix Value 51', D51)
print('Distance Matrix Value 52', D52)
print('Distance Matrix Value 53', D53)
print('Distance Matrix Value 54', D54)
print('Distance Matrix Value 55', D55)

print ('\n')
print ('Chlamydia_trachomatis',	'Escherichia_coli', 'Geobacter_sulfurreducens', 'Gloeobacter_violaceus', 'Saccharomyces_Cerevisiae', sep='\t')
print ( D11, D12, D13, D14, D15 ,sep='\t')
print ( D21, D22, D23, D24, D25 ,sep='\t')
print ( D31, D32, D33, D34, D35 ,sep='\t')
print ( D41, D42, D43, D44, D45 ,sep='\t')
print ( D51, D52, D53, D54, D55 ,sep='\t')
