
from Bio import SeqIO
print("----- FASTA File Scanner -----")
for record in SeqIO.parse("patient1.fasta.txt", "fasta"):
    print("Record ID:", record.id)
    print("Sequence Length:", len(record.seq), "base pairs")
    print("Actual Sequence:", record.seq)