import os
import sys
import glob
import pandas as pd

os.chdir(sys.path[0])
cwd = os.getcwd()
print(cwd)

csv_files = []

for m in glob.glob('./annotacje_bin.*'):
    for txt in glob.glob('./*.txt'):
        with open(txt) as t_file:
            f = t_file.readlines()
            # Extracting specific information from the text file
            for line in f:
                if line.startswith('CDS:'):
                    s_cds=line.split()
                    cds_int=int(s_cds[1])
                if line.startswith('proteins annotated:'):
                    s_pa=line.split()
                    pa_int=int(s_pa[2])
                if line.startswith('hypothetical proteins:'):
                    s_hp=line.split()
                    hp_int=int(s_hp[2])
                if line.startswith('bases:'):
                    s_b=line.split()
                    b_int=int(s_b[1])
                if line.startswith('contigs:'):
                    s_c=line.split()
                    c_int=int(s_c[1])
                if line.startswith('tRNA:'):
                    s_tRNA=line.split()
                    tRNA_int=int(s_tRNA[1])
                if line.startswith('rRNA:'):
                    s_rRNA=line.split()
                    rRNA_int=int(s_rRNA[1])
                if line.startswith('tmRNA:'):
                    s_tmRNA=line.split()
                    tmRNA_int=int(s_tmRNA[1])
            
            # Calculating the total RNA value
            try:
                tot_rna=tRNA_int+rRNA_int+tmRNA_int
            except NameError:
                pass
            
            # Creating a dictionary with the extracted values
            k=['CDS', 'proteins annotated', 'hypothetical proteins', 'bases', 'contigs', 'total RNA']
            v=[cds_int, pa_int, hp_int, b_int, c_int, tot_rna]
            ch_dict=dict(zip(k, v))

            #extracting bin numbers from file names and creating a nested dictionary
            lista_binow=[]
            filename=os.path.basename(m)
            bin_number=filename.split('_')[4]
            lista_binow.append(bin_number)
            p_dict=dict()
            p_dict=dict.fromkeys(lista_binow, ch_dict)

    # Creating a DataFrame and saving it as a CSV file
    df=pd.DataFrame(p_dict)
    df.to_csv(f"metaflye_{bin_number}.csv")
    
    # Collecting the CSV file names for later merging
    csv_files=[]
    for csv in glob.glob('./metaflye_*.csv'):
        csv_files.append(csv)

df2 = pd.DataFrame()

for file in csv_files:
    data = pd.read_csv(file)
    df2 = pd.concat([df2, data], axis=0)

df2.to_csv('merged_files.csv', index=False)