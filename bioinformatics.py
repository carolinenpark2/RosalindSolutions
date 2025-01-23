#count G in the dna sequence 
g = sequence.count('G')
#count C in the dna sequence 
c = sequence.count('C')
#calculate percent content
gc_content = (g + c) / len(sequence) * 100
gc_content
