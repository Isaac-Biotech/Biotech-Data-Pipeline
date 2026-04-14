
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
my_dna = Seq("ATGCGCGCGTATCGATAG")
gc_percentage = gc_fraction(my_dna) * 100
print(f"Professional GC Content: {gc_percentage:.2f}%")
