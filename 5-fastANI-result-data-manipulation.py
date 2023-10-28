import pandas as pd
import os

# loading the table
df=pd.read_table("C:/Users/aurin/Downloads/fastani-wynik.tsv")

# renaming wrong names of columns
df=df.append({'GUM10_metaspades_bin.10.permissive.fa': 'GUM10_metaspades_bin.10.permissive.fa', 'GUM10_metaspades_bin.10.permissive.fa.1': 'GUM10_metaspades_bin.10.permissive.fa.1',
           '100': '100', '1096': '1096', '1098': '1098'}, ignore_index=True)
df=df.rename(columns={'GUM10_metaspades_bin.10.permissive.fa': 'query', 'GUM10_metaspades_bin.10.permissive.fa.1': 'reference', '100': 
                   'completness', '1096': 'porównanie', '1098': 'pocięte'})

# counting unique values in a column
value_counts = df['query'].value_counts(dropna=True, sort=True)

# converting a Series to a DataFrame
df_val_counts = pd.DataFrame(value_counts)

# resetting the Index of a DataFrame
df_value_counts_reset = df_val_counts.reset_index()

# renaming columns of a DataFrame
df_value_counts_reset.columns = ['unique_values', 'counts']

# filtering rows based on column values
df_value_counts_13 = df_value_counts_reset[df_value_counts_reset['counts'] <= 13]

# Selecting a Column and Creating a DataFrame
df_value_13=df_value_counts_13['unique_values']
df_value_13=pd.DataFrame(data=df_value_13)
df_value_13=df_value_13.rename(columns={'unique_values': 'query'})

# merging DataFrames based on matching values in the 'query' column
result=df.merge(df_value_13)