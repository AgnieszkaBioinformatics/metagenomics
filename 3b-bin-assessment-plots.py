import pandas as pd
import os
from IPython.display import Image
import seaborn as sns

# create a list of files from the folder
metaspades_dir = os.listdir("C:/Users/aurin/Desktop/metaspades")
dfs = []  # List to store individual DataFrames

# reading all files from metaspades
for metaspades_file in metaspades_dir:
    metaspades_csv = pd.read_csv(f"C:/Users/aurin/Desktop/metaspades/{metaspades_file}")
    dfs.append(metaspades_csv.iloc[:, [1]])  # Append the first two columns of each DataFrame

# Concatenate the list of DataFrames into a single DataFrame
df_metaspades = pd.concat(dfs, axis=1)

# df transposing and formating to get the desired layout
df_metaspades=df_metaspades.T

df_metaspades=df_metaspades.rename({0: 'CDS'}, axis='columns')
df_metaspades=df_metaspades.rename({1: 'bases'}, axis='columns')
df_metaspades=df_metaspades.rename({2: 'contigs'}, axis='columns')
df_metaspades=df_metaspades.rename({3: 'hypothetical_proteins'}, axis='columns')
df_metaspades=df_metaspades.rename({4: 'proteins annotated'}, axis='columns')
df_metaspades=df_metaspades.rename({5: 'total_RNA'}, axis='columns')
df_metaspades['category']='metaspades'

# setting 'biny' column as index
df_metaspades['biny']=df_metaspades.index

# melt function to create a table with all the combinations of specified values
metaspades_melt = pd.melt(df_metaspades, id_vars=['contigs', 'CDS', 'bases', 'hypothetical_proteins', 'proteins annotated', 'total_RNA'], value_vars=['biny'])

# creating relational plots for data divided by number of contigs
CDS_metaspades=sns.relplot(
    data=metaspades_melt, x="CDS", y="hypothetical_proteins",
    col="contigs", hue="value", style='value', size="proteins annotated", sizes=(20, 500), kind="scatter", col_wrap=4, height=5)
CDS_metaspades=CDS_metaspades.set_titles(col_template="{col_name}", row_template="{row_name}")
CDS_metaspades.set_axis_labels("CDS", "hypothetical_proteins")

CDS_metaspades.fig.subplots_adjust(top=0.95)
CDS_metaspades.fig.suptitle('Metaspades - number of contigs', size=15)
CDS_metaspades.fig.subplots_adjust(wspace=0.5)
CDS_metaspades.fig.subplots_adjust(right=0.85)

# adding the right y-axis
for rna, ax in CDS_metaspades.axes_dict.items():  
    ax1 = ax.twinx()
    sns.lineplot(data=metaspades_melt, x='CDS', y='total_RNA', color='orange', ci=None, ax=ax1, lw=0.5)
    ax1.set_ylabel('total_RNA')
plt.savefig("C:/Users/aurin/Desktop/metaspades-bins.png")


# create a list of files from the folder
metaflye_dir=os.listdir("C:/Users/aurin/Desktop/metaflye")

dfss = []  # List to store individual DataFrames

# reading all files from metaflye
for metaflye_file in metaflye_dir:
    metaflye_csv = pd.read_csv(f"C:/Users/aurin/Desktop/metaflye/{metaflye_file}")
    dfss.append(metaflye_csv.iloc[:, [1]])  # Append the first two columns of each DataFrame

# Concatenate the list of DataFrames into a single DataFrame
df_metaflye = pd.concat(dfss, axis=1)

# df transposing and formating to get the desired layout
df_metaflye=df_metaflye.T
df_metaflye=df_metaflye.rename({0: 'CDS'}, axis='columns')
df_metaflye=df_metaflye.rename({1: 'bases'}, axis='columns')
df_metaflye=df_metaflye.rename({2: 'contigs'}, axis='columns')
df_metaflye=df_metaflye.rename({3: 'hypothetical_proteins'}, axis='columns')
df_metaflye=df_metaflye.rename({4: 'proteins annotated'}, axis='columns')
df_metaflye=df_metaflye.rename({5: 'total_RNA'}, axis='columns')
df_metaflye['kategoria']='metaflye'

# setting 'biny' column as index
df_metaflye['biny']=df_metaflye.index

# melt function to create a table with all the combinations of specified values
metaflye_melt = pd.melt(df_metaflye, id_vars=['CDS','hypothetical_proteins', 'proteins annotated', 'bases', 'contigs', 'total_RNA'], value_vars=['biny'])

# creating relational plots for data divided by number of contigs
CDS_metaflye=sns.relplot(
    data=metaflye_melt, x="CDS", y="hypothetical_proteins",
    col="contigs", hue="value", style='value', size="proteins annotated", sizes=(20, 500), kind="scatter", col_wrap=4, height=4)
CDS_metaflye=CDS_metaflye.set_titles(col_template="{col_name}", row_template="{row_name}")
CDS_metaflye.set_axis_labels("CDS", "hypothetical_proteins")

CDS_metaflye.fig.subplots_adjust(top=0.90)
CDS_metaflye.fig.suptitle('Metaflye - number of contigs', size=15)
CDS_metaflye.fig.subplots_adjust(wspace=0.5)
CDS_metaflye.fig.subplots_adjust(right=0.85)

for rna, ax in CDS_metaflye.axes_dict.items():  
    ax1 = ax.twinx()
    sns.lineplot(data=metaflye_melt, x='CDS', y='total_RNA', color='orange', ci=None, ax=ax1, lw=0.5)
    ax1.set_ylabel('total_RNA')
plt.savefig("C:/Users/aurin/Desktop/metaflye-bins.png")
