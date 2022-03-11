# out: ../$value/train/QC.fam .bed .bim ../$value/test/QC.fam .bed .bim
# in : $1 value $2 ../s1.train_getID.list $3 ../$value/snp.list $4 ../s1.test_getID.list

value=$1

# train
/zfssz2/ST_MCHRI/BIGDATA/USER/jxs/prs_Tutorial/software/plink/plink \
    --bfile /zfssz3/ST_MCHRI/BIGDATA/bigdata_ai/pub_data/PRS/UKB/UKB_impute/0.qc/impute_merge \
    --keep $2 \
    --make-bed \
    --autosome \
    --snps-only \
    --out ../$value/train/QC \
    --extract $3


#test
/zfssz2/ST_MCHRI/BIGDATA/USER/jxs/prs_Tutorial/software/plink/plink \
    --bfile /zfssz3/ST_MCHRI/BIGDATA/bigdata_ai/pub_data/PRS/UKB/UKB_impute/0.qc/impute_merge \
    --keep  $4\
    --make-bed \
    --autosome \
    --snps-only \
    --out ../$value/test/QC \
    --extract $3