
from Bio.Seq import Seq
my_dna = Seq("ATGTTTGTTTATCGATAG")
my_protein = my_dna.translate()
print("----- Biopython Translator -----")
print("Original DNA:", my_dna)
print("Protein Chain:", my_protein)
