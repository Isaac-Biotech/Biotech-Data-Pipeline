#12 and 13 were made for homework
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

# 1. Create our DNA sequence
my_dna = Seq("ATGCGCGCGTATCGATAG")


gc_percentage = gc_fraction(my_dna) * 100

print(f"Professional GC Content: {gc_percentage:.2f}%")