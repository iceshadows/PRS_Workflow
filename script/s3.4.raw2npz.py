import numpy as np
import csv
import sys
import os

value = sys.argv[1]
path = os.path.join("..",value)
train_raw = os.path.join(path,"train_ML.raw") 
test_raw = os.path.join(path,"test_ML.raw") 
train_npz = os.path.join(path,"train_ML.npz")
test_npz = os.path.join(path,"test_ML.npz")

def raw2npz(path):
    genotype = []
    phenotype = []
    sample_id = []
    snp_index = []
    with open(path, 'r') as f:
        lines = csv.reader((line.replace('NA', '0') for line in f), delimiter=' ')
        head = next(lines)
        for i, line in enumerate(lines):
            if(i%10000==0):
                print(i)
            genotype.append(np.array(line[head.index("PHENOTYPE")+1:]).astype("int"))
            phenotype.append(np.array(line[head.index("PHENOTYPE")]))
            sample_id.append(line[0])
        snp_index=head[head.index("PHENOTYPE")+1:]
    return genotype, phenotype, sample_id, snp_index
print("For:train")
train_genotype, train_phenotype, train_sample_id, train_snp_index=raw2npz(train_raw)
print("Saving..")
np.savez_compressed(train_npz,snps=train_genotype, lable=train_phenotype, sample_id=train_sample_id, snp_index=train_snp_index)
print("For:test")
test_genotype, test_phenotype, test_sample_id, test_snp_index=raw2npz(test_raw)
print("Saving..")
np.savez_compressed(test_npz,snps=test_genotype, lable=test_phenotype, sample_id=test_sample_id, snp_index=test_snp_index)
print("Done")
