#! /home/alexmakh/miniconda3/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

loc_oc43 = pd.DataFrame(pd.read_csv('Results/locus_Result_OC43.txt', sep='\t'))
loc_mers = pd.DataFrame(pd.read_csv('Results/locus_Result_MERS.txt', sep='\t'))
l_sars2 = pd.DataFrame(pd.read_csv('Results/locus_Result_SARS2.txt', sep='\t'))
loc_sars = pd.DataFrame(pd.read_csv('Results/locus_Result_SARS.txt', sep='\t'))

mirna = 'miR-21-3p'

x1 = loc_sars[loc_sars['miRNA'] == mirna]['MSA_start'].tolist()
y1 = loc_sars[loc_sars['miRNA'] == mirna]['MSA_end'].tolist()

x2 = loc_oc43[loc_oc43['miRNA'] == mirna]['MSA_start'].tolist()
y2 = loc_oc43[loc_oc43['miRNA'] == mirna]['MSA_end'].tolist()

x3 = l_sars2[l_sars2['miRNA'] == mirna]['MSA_start'].tolist()
y3 = l_sars2[l_sars2['miRNA'] == mirna]['MSA_end'].tolist()

x4 = loc_mers[loc_mers['miRNA'] == mirna]['MSA_start'].tolist()
y4 = loc_mers[loc_mers['miRNA'] == mirna]['MSA_end'].tolist()

fig, ax = plt.subplots(1, 1, figsize=(25, 25), tight_layout=True)
fig.suptitle('miR-21-3p conserved and nonconserved binding sites',
             va='baseline', color='blue')

ax.set_xlabel('Start nt of binding site', fontsize=15, color='blue')
ax.set_ylabel('End nt of binding site', fontsize=15, color='blue')

ax.yaxis.set_ticks(np.arange(0, 33001, 1000))
ax.xaxis.set_ticks(np.arange(0, 33001, 1000))
ax.yaxis.set_tick_params(labelsize=10)
ax.xaxis.set_tick_params(labelrotation=45, labelsize=10)
ax.axis([-1000, 33000, -1000, 33000])
ax.grid()

ax = plt.plot(x3, y3, 'og', markersize=12, label='SARS2')
ax = plt.plot(x1, y1, 'or', markersize=9, label='SARS')
ax = plt.plot(x2, y2, 'o', color='orange', markersize=6, label='OC43')
ax = plt.plot(x4, y4, 'o', color='purple', markersize=3, label='MERS')

plt.legend()

plt.show()
