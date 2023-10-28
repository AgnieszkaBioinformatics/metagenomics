import sys
import re
import os
import glob
import shutil

# current working directory
os.chdir(sys.path[0])  # retrieve the directory where the script is located
cwd = os.getcwd()

# file iteration
for m in glob.glob('./annotacje_bin.*'):
    # change the current working directory to each file's directory   
    bin_dir = os.chdir(f"{cwd}/{m}")
    print("dir", os.getcwd())    

# Processing GBK Files
for gbk in glob.glob("*.gbk"):
    with open(gbk, "r") as gbk_file:
        f = gbk_file.read()
        # The count for each GBK file.
        count_hypothetical = f.count('hypothetical protein')
        print("hypothetical proteins: ", count_hypothetical)

# Copying Text Files
for txt in glob.glob("*.txt"):
    shutil.copyfile(txt, f"{txt}.org")

    with open(txt, "a+") as cp:
        cp.seek(0) 
        for line in cp.readlines():
                if line.startswith("CDS:"):
                    splitting = line.split()
                    cds_int = int(splitting[1])
                    proteins_annotated = cds_int - int(count_hypothetical)
                    print(proteins_annotated)

        cp.seek(0, os.SEEK_END) 
        cp.write(f"proteins annotated: {proteins_annotated}\nhypothetical proteins: {count_hypothetical}\n")