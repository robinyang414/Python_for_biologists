# Using the data from part one, write a program that will calculate what percentage
# of the DNA sequence is coding.
# Part 1:

my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
p1 = 62
p2 = 91
exon1 = my_dna[0:p1]
exon2 = my_dna[p2-1:len(my_dna)]
print(len(exon1+exon2)/len(my_dna)*100)
