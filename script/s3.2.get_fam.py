#argv[1]:pvalue r1e-6
#output ../{pvalue}/train/QC.fam.new ../{pvalue}/test/QC.fam.new

import pandas as pd
import sys
import os

value = sys.argv[1].replace("r","")
print("For:",str(value))
print("For:","train")
# --train--
fam_path = os.path.join("..",value,"train","QC.fam")
fam_new_path =  os.path.join("..",value,"train","QC.fam.new")
pheno_path = os.path.join("..","s1.train_pheno.txt") 
print("Readding pheno...")
pheno_df = pd.read_csv(pheno_path, sep=' ', header=None)
pheno_df[2] = pheno_df[2].replace(1, 2).replace(0, 1)
print("Readding fam...")
fam_df = pd.read_csv(fam_path, sep=' ', header=None)

# new_df = pd.concat([fam_df, pheno_df], join='inner', axis=1)
new_df = pd.merge(fam_df, pheno_df, on=[0, 1])
new_df = new_df.drop(5, axis=1)
print("saving...")
new_df.to_csv(fam_new_path, sep=' ', index=False, header=None)

# --test--
print("For:","test")
fam_path = os.path.join("..",value,"test","QC.fam")
fam_new_path = os.path.join("..",value,"test","QC.fam.new")
pheno_path = os.path.join("..","s1.test_pheno.txt") 
print("Readding pheno...")
pheno_df = pd.read_csv(pheno_path, sep=' ', header=None)
pheno_df[2] = pheno_df[2].replace(1, 2).replace(0, 1)
print("Readding fam...")
fam_df = pd.read_csv(fam_path, sep=' ', header=None)

# new_df = pd.concat([fam_df, pheno_df], join='inner', axis=1)
new_df = pd.merge(fam_df, pheno_df, on=[0, 1])
new_df = new_df.drop(5, axis=1)
print("saving...")
new_df.to_csv(fam_new_path, sep=' ', index=False, header=None)
print("Done")
