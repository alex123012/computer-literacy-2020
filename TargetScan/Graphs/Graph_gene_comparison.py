#! /home/alexmakh/miniconda3/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

loc_oc43 = pd.DataFrame(pd.read_csv('Results/locus_Result_OC43.txt', sep='\t'))
loc_mers = pd.DataFrame(pd.read_csv('Results/locus_Result_MERS.txt', sep='\t'))
l_sars2 = pd.DataFrame(pd.read_csv('Results/locus_Result_SARS2.txt', sep='\t'))
loc_sars = pd.DataFrame(pd.read_csv('Results/locus_Result_SARS.txt', sep='\t'))

fig, axs = plt.subplots(2, 4, figsize=(25, 12.5), tight_layout=True)
fig.suptitle('Genes that binds miRNA', va='baseline', color='blue')

fon = 10
mark = 7

axs[0, 0].set_title('SARS-2\nmiR-21-3p', color='green')
axs[0, 0].set_xlabel('start position in RNA sequence',
                     color='green')
axs[0, 0].set_ylabel('end position in RNA sequence',
                     color='green')
data = l_sars2[l_sars2['miRNA'] == 'miR-21-3p']
x = data['Locus_start'].tolist()
y = data['Locus_end'].tolist()
axs[0, 0].yaxis.set_tick_params(labelsize=fon)
axs[0, 0].xaxis.set_tick_params(labelrotation=45, labelsize=fon)
axs[0, 0].grid()
axs[0, 0].plot(x, y, 'og', markersize=mark)

axs[1, 0].set_title('miR-16-5p', color='red')
axs[1, 0].set_xlabel('start position in RNA sequence',
                     color='red')
axs[1, 0].set_ylabel('end position in RNA sequence',
                     color='red')
data = l_sars2[l_sars2['miRNA'] == 'miR-16-5p']
x1 = data['Locus_start'].tolist()
y1 = data['Locus_end'].tolist()
axs[1, 0].yaxis.set_tick_params(labelsize=fon)
axs[1, 0].xaxis.set_tick_params(labelrotation=45, labelsize=fon)
axs[1, 0].grid()
axs[1, 0].plot(x1, y1, 'or', markersize=mark)

axs[0, 1].set_title('SARS\nmiR-21-3p', color='green')
axs[0, 1].set_xlabel('start position in RNA sequence',
                     color='green')
axs[0, 1].set_ylabel('end position in RNA sequence',
                     color='green')
data = loc_sars[loc_sars['miRNA'] == 'miR-21-3p']
x = data['Locus_start'].tolist()
y = data['Locus_end'].tolist()
axs[0, 1].yaxis.set_tick_params(labelsize=fon)
axs[0, 1].xaxis.set_tick_params(labelrotation=45, labelsize=fon)
axs[0, 1].grid()
axs[0, 1].plot(x, y, 'og', markersize=mark)

axs[1, 1].set_title('miR-16-5p', color='red')
axs[1, 1].set_xlabel('start position in RNA sequence',
                     color='red')
axs[1, 1].set_ylabel('end position in RNA sequence',
                     color='red')
data = loc_sars[loc_sars['miRNA'] == 'miR-16-5p']
x = data['Locus_start'].tolist()
y = data['Locus_end'].tolist()
axs[1, 1].yaxis.set_tick_params(labelsize=fon)
axs[1, 1].xaxis.set_tick_params(labelrotation=45, labelsize=fon)
axs[1, 1].grid()
axs[1, 1].plot(x, y, 'or', markersize=mark)

axs[0, 2].set_title('MERS\nmiR-21-3p', color='green')
axs[0, 2].set_xlabel('start position in RNA sequence',
                     color='green')
axs[0, 2].set_ylabel('end position in RNA sequence',
                     color='green')
data = loc_mers[loc_mers['miRNA'] == 'miR-21-3p']
x = data['Locus_start'].tolist()
y = data['Locus_end'].tolist()
axs[0, 2].yaxis.set_tick_params(labelsize=fon)
axs[0, 2].xaxis.set_tick_params(labelrotation=45, labelsize=fon)
axs[0, 2].grid()
axs[0, 2].plot(x, y, 'og', markersize=mark)

axs[1, 2].set_title('miR-16-5p', color='red')
axs[1, 2].set_xlabel('start position in RNA sequence',
                     color='red')
axs[1, 2].set_ylabel('end position in RNA sequence',
                     color='red')
data = loc_mers[loc_mers['miRNA'] == 'miR-16-5p']
x = data['Locus_start'].tolist()
y = data['Locus_end'].tolist()
axs[1, 2].yaxis.set_tick_params(labelsize=fon)
axs[1, 2].xaxis.set_tick_params(labelrotation=45, labelsize=fon)
axs[1, 2].grid()
axs[1, 2].plot(x1, y1, 'or', markersize=mark)

axs[0, 3].set_title('OC43\nmiR-21-3p', color='green')
axs[0, 3].set_xlabel('start position in RNA sequence',
                     color='green')
axs[0, 3].set_ylabel('end position in RNA sequence',
                     color='green')
data = loc_oc43[loc_oc43['miRNA'] == 'miR-21-3p']
x = data['Locus_start'].tolist()
y = data['Locus_end'].tolist()
axs[0, 3].yaxis.set_tick_params(labelsize=fon)
axs[0, 3].xaxis.set_tick_params(labelrotation=45, labelsize=fon)
axs[0, 3].grid()
axs[0, 3].plot(x, y, 'og', markersize=mark)

axs[1, 3].set_title('miR-16-5p', color='red')
axs[1, 3].set_xlabel('start position in RNA sequence',
                     color='red')
axs[1, 3].set_ylabel('end position in RNA sequence',
                     color='red')
data = loc_oc43[loc_oc43['miRNA'] == 'miR-16-5p']
x = data['Locus_start'].tolist()
y = data['Locus_end'].tolist()
axs[1, 3].yaxis.set_tick_params(labelsize=fon)
axs[1, 3].xaxis.set_tick_params(labelrotation=45, labelsize=fon)
axs[1, 3].grid()
axs[1, 3].plot(x1, y1, 'or', markersize=mark)
plt.show()
