# input: phenotype race, output: s2.gwas_train_result.fastGWA

/zfssz2/ST_MCHRI/BIGDATA/USER/jxs/software/gcta_1.93.3beta2/gcta64 \
 --bfile /zfssz3/ST_MCHRI/BIGDATA/bigdata_ai/pub_data/PRS/UKB/UKB_impute/0.qc/impute_merge \
 --grm-sparse $1 \
 --fastGWA-mlm-binary \
 --pheno $2 \
 --keep $3 \
 --qcovar $4 \
 --covar $5   \
 --threads 5 \
 --out $6 \
 --maf 0.01 \
 --geno 0.1 