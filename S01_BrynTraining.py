"""
Py script to Teach Basic Coding
"""

# ==============================================================================

__title__ = "Training Script: Basic Coding"
__author__ = "Arden Burrell"
__version__ = "v1.0(22.05.2025)"
__email__ = "arden.burrell@sydney.edu.au"


# ==============================================================================

import os
import sys
import argparse
import pathlib
import git
# from git import exc as git_exc

# ==============================================================================
# ========== Import packages ==========
import numpy as np
import pandas as pd
import yaml
# import ipdb
# ========== Import plotting packages ==========

import matplotlib.pyplot as plt
import seaborn as sns       


# ==============================================================================
# randomstr = "20251110"
# gamma_csv_path =f"MOLE_DATA/Gamma_{randomstr}.csv"
#df = pd.read_csv("MOLE_DATA/Gamma_20251110.csv")
# gamma_df = pd.read_csv(gamma_csv_path,  encoding='Latin-1', skiprows=2 ,index_col=False) 
gamma_csv_path = "MOLE_DATA/GammaMarchT3.csv"
gamma_df = pd.read_csv(gamma_csv_path,index_col=False) 
# print(gamma_df)

#===============================================================================

# Convert UtcDate and UtcTime into a single pandas Timestamp
# Combine UtcDate and UtcTime columns into a datetime string
gamma_df['DateTime'] = pd.to_datetime(gamma_df['UtcDate'].astype(str) + ' ' + gamma_df['UtcTime'].astype(str))
print(gamma_df["DateTime"])

# ================================================================================
# Plot time vs TOTAL_GMM [cps] using seaborn
df_subset = gamma_df[['DateTime', 'TotCount.cps.','Thorium.ppm.', 'Uranium.ppm.', 'Potassium...']]
# breakpoint()

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_subset, x='DateTime', y='TotCount.cps.')
plt.title('TOTAL_GMM [cps] over Time')
plt.xlabel('Time (UTC)')
plt.ylabel('TOTAL_GMM [cps]')
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()

sns.relplot(data=df_subset, x="Thorium.ppm.", y="Uranium.ppm.", )
plt.show()


