def translate_dna(Dna_data):
    print("You dna is stolen protocal is on"+Dna_data)
    codon_table = {
        "ATG": "M",
        "CGT": "R",
        "AGC":"T",
        "TAG":"*",
        "CTA":"L",
        "GCT":"A",
        "AGC":"S",
        "CGG":"R",
        "GGG":"G",
        "GTT":"V",
        "TTA":"L",


    }
    with open (Dna_data,"r") as my_file:
        dna = my_file.read().strip()

    protein = ""
    for i in range(0, len(dna), 3):
        codon = dna [i:i+3]
        amino_acid = codon_table.get(codon,"?")
        protein = protein + amino_acid
    print("--------Translation Conpleat")
    print("DNA-stolen :"+dna)
    print("Proten sequence :" + protein)
translate_dna("Dna_data.txt")
