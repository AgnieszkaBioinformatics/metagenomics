import pandas as pd
import os
from IPython.display import Image

# loading the table 
bin_spades_fly=pd.read_csv("C:/Users/aurin/Downloads/bin_spades_to_flay.tsv", sep='\t')

# cleaning the table from non-paired (taxonomically unique) bins 

for index, row in bin_spades_fly.iterrows():
    if '-' in row.values:
        bin_spades_fly.drop(index, inplace=True)

bin_spades_fly.drop(index=29, inplace=True)

# creating new df with column of metaspades bins
df_bin_muffin_metaspades=bin_spades_fly['bin_muffin_metaspades']
df_bin_muffin_metaspades=pd.DataFrame(data=df_bin_muffin_metaspades)
df_bin_muffin_metaspades=df_bin_muffin_metaspades.set_index('bin_muffin_metaspades')

# creating new df with column of metaflye bins
df_bin_muffin_metaflye=bin_spades_fly['bin_muffin_metaflay']
df_bin_muffin_metaflye=pd.DataFrame(data=df_bin_muffin_metaflye)
df_bin_muffin_metaflye=df_bin_muffin_metaflye.set_index('bin_muffin_metaflay')

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
df_metaspades['biny']=df_metaspades.index
df_metaspades=df_metaspades.reset_index(drop=True)

# finding the bins that are common among two tables
common_bins_metaspades = bin_spades_fly['bin_muffin_metaspades'].isin(df_metaspades['biny'])

# Print the resulting data frame
print(common_bins_metaspades)

# cutting common bins to new dfs
matched_bins_metaspades07 = df_metaspades.iloc[0:8].values
print(matched_bins_metaspades07)
#[12, 14, 18, 19, 20, 21, 22, 23, 24]]
matched_bins_metaspades12 = df_metaspades.iloc[12].values
matched_bins_metaspades1415=df_metaspades.iloc[14:16].values
matched_bins_metaspades1824=df_metaspades.iloc[18:].values

matched_bins_metaspades07=pd.DataFrame(data=matched_bins_metaspades07)
matched_bins_metaspades12=pd.DataFrame(data=matched_bins_metaspades12)
matched_bins_metaspades1415=pd.DataFrame(data=matched_bins_metaspades1415)
matched_bins_metaspades1824=pd.DataFrame(data=matched_bins_metaspades1824)

# renaming columns
matched_bins_metaspades07.rename(columns={0: 'CDS', 1: 'bases', 2: 'contigs', 3: 'hypothetical proteins', 4: 'proteins annotated', 
5: 'total RNA', 6: 'kategoria', 7: 'biny'}, inplace=True)

matched_bins_metaspades12=matched_bins_metaspades12.T
matched_bins_metaspades12.rename(columns={0: 'CDS', 1: 'bases', 2: 'contigs', 3: 'hypothetical proteins', 4: 'proteins annotated', 
5: 'total RNA', 6: 'kategoria', 7: 'biny'}, inplace=True)

matched_bins_metaspades1415.rename(columns={0: 'CDS', 1: 'bases', 2: 'contigs', 3: 'hypothetical proteins', 4: 'proteins annotated', 
5: 'total RNA', 6: 'kategoria', 7: 'biny'}, inplace=True)

matched_bins_metaspades1824.rename(columns={0: 'CDS', 1: 'bases', 2: 'contigs', 3: 'hypothetical proteins', 4: 'proteins annotated', 
5: 'total RNA', 6: 'kategoria', 7: 'biny'}, inplace=True)

# concatenating dfs
matched_bins_metaspades_conc=pd.concat([matched_bins_metaspades07, matched_bins_metaspades12, matched_bins_metaspades1415, matched_bins_metaspades1824])
matched_bins_metaspades_conc.set_index('biny', inplace=True)
matched_bins_metaspades_conc=matched_bins_metaspades_conc.reindex(df_bin_muffin_metaspades.index)

# create a list of files from the folder
metaflye_dir=os.listdir("C:/Users/aurin/Desktop/metaflye")

dfss = []  # List to store individual DataFrames

for metaflye_file in metaflye_dir:
    metaflye_csv = pd.read_csv(f"C:/Users/aurin/Desktop/metaflye/{metaflye_file}")
    dfss.append(metaflye_csv.iloc[:, [1]])  # Append the first two columns of each DataFrame

metaflye_csv.iloc[:, [0]].rename({'Unnamed: 0': 'features'}, axis='columns')
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

# set 'biny' as index
df_metaflye['biny']=df_metaflye.index

# finding the bins that are common among two tables
common_bins_metaflye = bin_spades_fly['bin_muffin_metaflay'].isin(df_metaflye['biny'])

# cutting common bins to new dfs
matched_bins_metaflye07 = df_metaflye.iloc[0:8].values
print(matched_bins_metaflye07)
#[12, 14, 18, 19, 20, 21, 22, 23, 24]]
matched_bins_metaflye12 = df_metaflye.iloc[12].values
matched_bins_metaflye1415=df_metaflye.iloc[14:16].values
matched_bins_metaflye1824=df_metaflye.iloc[18:24].values

matched_bins_metaflye07=pd.DataFrame(data=matched_bins_metaflye07)
matched_bins_metaflye12=pd.DataFrame(data=matched_bins_metaflye12)
matched_bins_metaflye1415=pd.DataFrame(data=matched_bins_metaflye1415)
matched_bins_metaflye1824=pd.DataFrame(data=matched_bins_metaflye1824)

# df transposing and formating to get the desired layout
matched_bins_metaflye07.rename(columns={0: 'CDS', 1: 'bases', 2: 'contigs', 3: 'hypothetical proteins', 4: 'proteins annotated', 
5: 'total RNA', 6: 'kategoria', 7: 'biny'}, inplace=True)

matched_bins_metaflye12=matched_bins_metaflye12.T
matched_bins_metaflye12.rename(columns={0: 'CDS', 1: 'bases', 2: 'contigs', 3: 'hypothetical proteins', 4: 'proteins annotated', 
5: 'total RNA', 6: 'kategoria', 7: 'biny'}, inplace=True)

matched_bins_metaflye1415.rename(columns={0: 'CDS', 1: 'bases', 2: 'contigs', 3: 'hypothetical proteins', 4: 'proteins annotated', 
5: 'total RNA', 6: 'kategoria', 7: 'biny'}, inplace=True)

matched_bins_metaflye1824.rename(columns={0: 'CDS', 1: 'bases', 2: 'contigs', 3: 'hypothetical proteins', 4: 'proteins annotated', 
5: 'total RNA', 6: 'kategoria', 7: 'biny'}, inplace=True)


# concatenating dfs
matched_bins_metaflye_conc=pd.concat([matched_bins_metaflye07, matched_bins_metaflye12, matched_bins_metaflye1415, matched_bins_metaflye1824])


# set new index of the df according to the index from df_bin_muffin_metaflye to get the order of corresponding bins
matched_bins_metaflye_conc.set_index('biny', inplace=True)
matched_bins_metaflye_conc=matched_bins_metaflye_conc.reindex(df_bin_muffin_metaflye.index)

# deleting bins with NaN values (will add them later)
matched_bins_metaflye_conc=matched_bins_metaflye_conc.drop('bin.5')
matched_bins_metaflye_conc=matched_bins_metaflye_conc.drop('bin.2')
matched_bins_metaflye_conc=matched_bins_metaflye_conc.drop('bin.18')
matched_bins_metaflye_conc=matched_bins_metaflye_conc.drop('bin.20')
matched_bins_metaflye_conc=matched_bins_metaflye_conc.drop('bin.19')
matched_bins_metaflye_conc=matched_bins_metaflye_conc.drop('bin.6')

# resetting index
matched_bins_metaflye_conc.reset_index(inplace=True)

# adding previously deleted data...
b5=pd.DataFrame({'bin_muffin_metaflay': 'bin.5', 'CDS': 2687, 'bases': 3209974, 'contigs': 2, 'hypothetical proteins': 1442, 
'proteins annotated': 1245, 'total RNA': 44, 'kategoria': 'metaflye'}, index=[0])
b18=pd.DataFrame({'bin_muffin_metaflay': 'bin.18', 'CDS': 2886,	'bases': 3409711, 'contigs': 1, 'hypothetical proteins': 1513,
'proteins annotated':	1373, 'total RNA': 43,'kategoria': 'metaflye'}, index=[0])
b20=pd.DataFrame({'bin_muffin_metaflay': 'bin.20','CDS': 4631,'bases': 5565142,	'contigs': 1,'hypothetical proteins': 2376,	
'proteins annotated': 2255,	'total RNA': 53,'kategoria': 'metaflye'}, index=[0])
b19=pd.DataFrame({'bin_muffin_metaflay':'bin.19','CDS':	3655,'bases':	4029707,'contigs':	2,'hypothetical proteins': 	1439,
'proteins annotated':	2216,'total RNA': 	61,'kategoria':	'metaflye'}, index=[0])
b6=pd.DataFrame({'bin_muffin_metaflay':'bin.6','CDS':	3951,'bases':	4526987,'contigs':	4,'hypothetical proteins': 	1637,
'proteins annotated':	2314,'total RNA':	59,'kategoria':	'metaflye'}, index=[0])
b2=pd.DataFrame({'bin_muffin_metaflay':'bin.2','CDS':	3689,'bases':	3917429,'contigs': 	2,'hypothetical proteins':	1321,
'proteins annotated':	2368,'total RNA':	56, 'kategoria': 'metaflye'}, index=[0])	
matched_bins_metaflye_conc = pd.concat([matched_bins_metaflye_conc, b5], ignore_index=True)
matched_bins_metaflye_conc = pd.concat([matched_bins_metaflye_conc, b18], ignore_index=True)
matched_bins_metaflye_conc = pd.concat([matched_bins_metaflye_conc, b20], ignore_index=True)
matched_bins_metaflye_conc = pd.concat([matched_bins_metaflye_conc, b19], ignore_index=True)
matched_bins_metaflye_conc = pd.concat([matched_bins_metaflye_conc, b6], ignore_index=True)
matched_bins_metaflye_conc = pd.concat([matched_bins_metaflye_conc, b2], ignore_index=True)

# set new index of the df according to the index from df_bin_muffin_metaflye to get the order of corresponding bins
matched_bins_metaflye_conc.set_index('bin_muffin_metaflay', inplace=True)
matched_bins_metaflye_conc=matched_bins_metaflye_conc.reindex(df_bin_muffin_metaflye.index)

# deleting unnecessary data
matched_bins_metaflye_conc=matched_bins_metaflye_conc.drop(columns=['proteins annotated', 'kategoria'])

matched_bins_metaspades_conc=matched_bins_metaspades_conc.drop(columns=['proteins annotated', 'kategoria'])