############## Distance Matrix Nucleotide and Dinucleotide content #############
import math
dic_dinuc1 = {}
dic_dinuc2 = {}
dic_dinuc3 = {}
dic_dinuc4 = {}
dic_dinuc5 = {}

dic_nuc1 = {}
dic_nuc2 = {}
dic_nuc3 = {}
dic_nuc4 = {}
dic_nuc5 = {}

#05.txt
#Dinucleotide Frequency
AG1= 7.4004
GC1= 4.962
CC1= 4.435
CA1= 6.047
AA1= 10.35
GA1= 7.21693
AC1= 4.778
GG1= 4.485
TA1= 6.821
AT1= 7.907
TG1= 6.001
GT1= 4.721
TC1= 7.192
CT1= 7.386
TT1= 10.28
CG1= 3.49969

#Nucleotide Frequency
A1= 29.415133324508343
G1= 20.663716050164318
C1= 20.646641611366586
T1= 29.274509013960753

#09.txt
#Dinucleotide Frequency
AG2= 5.5883
GC2= 8.7429
CC2= 6.3737
CA2= 7.5885
AA2= 7.8190
GA2= 6.2548
AC2= 5.9688
GG2= 6.3193
TA2= 4.9430
AT2= 7.2291
TG2= 7.5206
GT2= 5.9474
TC2= 6.2692
CT2= 5.5563
TT2= 7.8784
CG2= 7.8362

#Nucleotide Frequency
A2= 24.67211307763248
G2= 25.283355439858617
C2= 25.36699893815194
T2= 24.677532544356957

#11.txt
#Dinucleotide Frequency
AG3= 6.0699
GC3= 9.68951
CC3= 10.3129
CA3= 6.83913
AA3= 5.08337
GA3= 7.5726
AC3= 5.60068
GG3= 10.1793
TA3= 2.43425
AT3= 5.17541
TG3= 6.789385
GT3= 5.609361
TC3= 7.576245
CT3= 6.015107
TT3= 5.052669
CG3= 10.01226

A3= 19.93358429455659
G3= 30.042919583234656
C3= 30.159753913993896
T3= 19.86374220821486

#12.txt
#Dinucleotide Frequency
AG4= 6.15691
GC4= 12.1660
CC4= 9.99234
CA4= 6.93252
AA4= 5.19390
GA4= 6.82375
AC4= 5.60810
GG4= 9.98498
TA4= 2.31386
AT4= 4.30513
TG4= 6.86470
GT4= 5.60429
TC4= 6.82701
CT4= 6.09615
TT4= 5.13025
CG4= 11.5724

#Nucleotide Frequency
A4= 19.058540005954043
G4= 30.99246858619808
C4= 31.00538976123514
T4= 18.94360164661273

#28.txt
#Dinucleotide Frequency
AG5= 5.97927
GC5= 3.89711
CC5= 4.09472
CA5= 6.81551
AA5= 11.1855
GA5= 6.35545
AC5= 5.57599
GG5= 4.00187
TA5= 7.51493
AT5= 9.13063
TG5= 6.66002
GT5= 5.43094
TC5= 6.41351
CT5= 6.02689
TT5= 10.9175
CG5= 3.04439

#Nucleotide Frequency
A5= 30.92973697353384
G5= 19.103943353067578
C5= 19.391159225299166
T5= 30.575160448099414

#Dinucleotide Dictionary
dic_dinuc1['AG']= AG1
dic_dinuc2['AG']= AG2
dic_dinuc3['AG']= AG3
dic_dinuc4['AG']= AG4
dic_dinuc5['AG']= AG5

dic_dinuc1['GC']=GC1
dic_dinuc2['GC']=GC2
dic_dinuc3['GC']=GC3
dic_dinuc4['GC']=GC4
dic_dinuc5['GC']=GC5

dic_dinuc1['CC']=CC1
dic_dinuc2['CC']=CC2
dic_dinuc3['CC']=CC3
dic_dinuc4['CC']=CC4
dic_dinuc5['CC']=CC5

dic_dinuc1['CA']=CA1
dic_dinuc2['CA']=CA2
dic_dinuc3['CA']=CA3
dic_dinuc4['CA']=CA4
dic_dinuc5['CA']=CA5

dic_dinuc1['AA']=AA1
dic_dinuc2['AA']=AA2
dic_dinuc3['AA']=AA3
dic_dinuc4['AA']=AA4
dic_dinuc5['AA']=AA5

dic_dinuc1['GA']=GA1
dic_dinuc2['GA']=GA2
dic_dinuc3['GA']=GA3
dic_dinuc4['GA']=GA4
dic_dinuc5['GA']=GA5

dic_dinuc1['AC']=AC1
dic_dinuc2['AC']=AC2
dic_dinuc3['AC']=AC3
dic_dinuc4['AC']=AC4
dic_dinuc5['AC']=AC5

dic_dinuc1['GG']=GG1
dic_dinuc2['GG']=GG2
dic_dinuc3['GG']=GG3
dic_dinuc4['GG']=GG4
dic_dinuc5['GG']=GG5

dic_dinuc1['TA']=TA1
dic_dinuc2['TA']=TA2
dic_dinuc3['TA']=TA3
dic_dinuc4['TA']=TA4
dic_dinuc5['TA']=TA5

dic_dinuc1['AT']=AT1
dic_dinuc2['AT']=AT2
dic_dinuc3['AT']=AT3
dic_dinuc4['AT']=AT4
dic_dinuc5['AT']=AT5

dic_dinuc1['TG']=TG1
dic_dinuc2['TG']=TG2
dic_dinuc3['TG']=TG3
dic_dinuc4['TG']=TG4
dic_dinuc5['TG']=TG5

dic_dinuc1['GT']=GT1
dic_dinuc2['GT']=GT2
dic_dinuc3['GT']=GT3
dic_dinuc4['GT']=GT4
dic_dinuc5['GT']=GT5

dic_dinuc1['TC']=TC1
dic_dinuc2['TC']=TC2
dic_dinuc3['TC']=TC3
dic_dinuc4['TC']=TC4
dic_dinuc5['TC']=TC5

dic_dinuc1['CT']=CT1
dic_dinuc2['CT']=CT2
dic_dinuc3['CT']=CT3
dic_dinuc4['CT']=CT4
dic_dinuc5['CT']=CT5

dic_dinuc1['TT']=TT1
dic_dinuc2['TT']=TT2
dic_dinuc3['TT']=TT3
dic_dinuc4['TT']=TT4
dic_dinuc5['TT']=TT5

dic_dinuc1['CG']=CG1
dic_dinuc2['CG']=CG2
dic_dinuc3['CG']=CG3
dic_dinuc4['CG']=CG4
dic_dinuc5['CG']=CG5


#Nucleotide Dictionary
dic_nuc1['A']= A1
dic_nuc2['A']= A2
dic_nuc3['A']= A3
dic_nuc4['A']= A4
dic_nuc5['A']= A5

dic_nuc1['G']= G1
dic_nuc2['G']= G2
dic_nuc3['G']= G3
dic_nuc4['G']= G4
dic_nuc5['G']= G5

dic_nuc1['C']= C1
dic_nuc2['C']= C2
dic_nuc3['C']= C3
dic_nuc4['C']= C4
dic_nuc5['C']= C5

dic_nuc1['T']= T1
dic_nuc2['T']= T5
dic_nuc3['T']= T5
dic_nuc4['T']= T5
dic_nuc5['T']= T5

##### Dinucleotide Distance Values ####
list_diffDN=[]
for key in dic_dinuc1:
	if key in dic_dinuc1:
		diffDN = (dic_dinuc1[key] - dic_dinuc2[key])
		#print(diffDN)
		diff_squareDN=diffDN**2
		#print(diff_squareDN)
		list_diffDN.append(diff_squareDN)
#print (list_diffDN)
total_diffDN = sum(list_diffDN)
#print(total_diffDN)

square_rootDN = math.sqrt(float(int(total_diffDN)))

print('For Dinucleotide Distance: G1-G2')
print(square_rootDN)

##### Nucleotide Distance Values ####
list_diffN=[]
for key in dic_nuc4:
	if key in dic_nuc5:
		diffN = (dic_nuc4[key] - dic_nuc5[key])
		#print(diffN)
		diff_squareN=diffN**2
		#print(diff_squareN)
		list_diffN.append(diff_squareN)
#print (list_diffN)
total_diffN = sum(list_diffN)
#print(total_diffN)

square_rootN = math.sqrt(float(int(total_diffN)))

print('For Nucleotide Distance: G4-G5')
print(square_rootN)
#print(dic_nuc1)
#print(dic_nuc2)
print('\n')
