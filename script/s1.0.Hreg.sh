#input pheno,keep,race
/zfssz2/ST_MCHRI/BIGDATA/USER/jxs/software/gcta_1.93.3beta2/gcta64 \
--HEreg \
--grm /zfssz3/ST_MCHRI/BIGDATA/bigdata_ai/pub_data/PRS/UKB/UKB_impute/1.grn/1.$3/temp \
--pheno $2 \
--keep $1 \
--out ../HEreg \
--thread-num 5