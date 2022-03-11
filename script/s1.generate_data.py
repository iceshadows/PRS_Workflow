import pandas as pd
from sklearn.utils import shuffle
import os
from sys import argv
'''
argv[1] : input s0.pheno.txt
argv[2] : seed
argv[3] : path

split ratio: 0.8
'''
seed = int(argv[2])
path = argv[3]
file = argv[1]
df = pd.read_csv(file, sep=' ', header=None)
df = df.dropna()
df = df.astype(int)
df.to_csv(path + 's1.all_valid_pheno.txt', sep=' ', index=False,header=None)

df = shuffle(df, random_state=seed)

length = len(df)
train_length = int(length*0.8)
test_length = length - train_length
train_length, test_length

train = df.iloc[0:train_length]
test =df.iloc[train_length:length]

train[[0,1]].to_csv(path + 's1.train_getID.list', sep=' ', index=False,header=None)
test[[0,1]].to_csv(path + 's1.test_getID.list', sep=' ', index=False,header=None)
train.to_csv(path + 's1.train_pheno.txt', sep=' ', index=False,header=None)
test.to_csv(path + 's1.test_pheno.txt', sep=' ', index=False,header=None)
