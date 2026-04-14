def anlize_dna(dna_data):
   print("Open the doors to hell:" + dna_data )
   with open (dna_data,"r")as my_file:
    dna = my_file.read().strip()
    g_count = dna.count("G")
    c_count = dna.count("C")
    total_len = len(dna)
    gc_percent=(g_count + c_count) / total_len*100
    print("stuff done")
    print("dna sequence" + dna)
    print("total bases"+str(total_len))
    print("GC persent:" + str(gc_percent) + "%")

anlize_dna("dna_data.txt")
