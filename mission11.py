import os
def batch_exerment_folder(folder_path):
    print("-------- Actvating batch prosses----")
    for file_name in os.listdir(folder_path):
        if file_name.endswith("txt"):
            with open(file_name,"r") as my_file:
                dna = my_file.read().strip()
            g_count = dna.count("G")
            C_count = dna.count("C")
            total_len = len(dna)
            if total_len >0:
                gc_percent=(g_count + C_count) / total_len *100
                print(file_name + "GC Content:" +str(round(gc_percent,2))+ "%")
batch_exerment_folder(".")

