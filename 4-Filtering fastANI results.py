import pandas as pd
import re

# data loading
ani = pd.read_table("C:/Users/aurin/Downloads/muffin_metaspades_bins_ani.tsv")

# column renaming
ani = ani.rename(columns={'GUM5_metaspades_bin.16.fa': 'reference', 'GUM5_metaspades_bin.16.fa.1': 'query', '100': 'ANI', '1443': 'nałożone', '1451': 'ilość'})

# data filtering
patternmetaflye = "(GUM5_metaflye_bin\..+\.fa)"
patternmetaspades = "(GUM.+_metaspades_bin\..+\.fa)"
filter = ani['reference'].str.contains(patternmetaflye)
filt = ani['query'].str.contains(patternmetaspades)
ani = ani[filter]
ani = ani[filt]
ani = ani.reset_index()

# data export
ani.to_csv("C:/Users/aurin/Desktop/porownanie.csv")