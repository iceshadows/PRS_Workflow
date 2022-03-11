"""
argv[1]:s0.output
argv[2]:race path
argv[3]:keep path
argv[4]:pheno path

"""
import pandas as pd
import numpy as np
from collections import Counter
from sys import argv
import os
keep_raw = pd.read_csv(argv[1],names=["IID","label"],header=0)
keep_case_id = set(keep_raw[keep_raw["label"]==1]["IID"])
keep_control_id = set(keep_raw[keep_raw["label"]==0]["IID"])
false_case = keep_case_id.intersection(keep_control_id)
keep_control_id.symmetric_difference_update(false_case)
keep_control = pd.DataFrame({
    "IID":list(keep_control_id),
    "label":0
})
keep_case = pd.DataFrame({
    "IID":list(keep_case_id),
    "label":1
})
keep = pd.concat((keep_case,keep_control),axis=0)
white_sample = pd.read_csv(argv[2],delimiter=" ",names=["FID","IID"])
white_sample.drop_duplicates(subset=["IID"],keep="first")
new=pd.merge(white_sample,keep,on="IID",validate="one_to_one",how='left')
print(new.value_counts("label"))
with open(argv[4],"w") as f:
    with open(argv[3],"w") as fd:
        for i,d in new.iterrows():
            iid = int(d["IID"])
            label = d["label"]
            try:
                label = int(label)
            except:
                label = "NA"
            fd.write("{} {}\n".format(str(iid),str(iid)))
            f.write("{} {} {}\n".format(str(iid),str(iid),str(label)))
print("Done")
