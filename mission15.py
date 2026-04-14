# Mission 14 and 15 took a day to code
from Bio import Entrez
Entrez.email = "isaac.shepley0@gmail.com"
print("----- Global Database Link Active -----")
print("Connecting to NCBI... ")
handle = Entrez.efetch(db="nucleotide", id="NM_000518", rettype="fasta", retmode="text")
raw_data = handle.read()
handle.close() 
print("\n--- Download Complete ---")
print("Raw Gene Data:")
print(raw_data[:500])
print("... [Gene sequence continues]")