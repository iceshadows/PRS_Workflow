# input ../$value/train/QC.fam ../$value/train/QC.fam.new ../$value/test/QC.fam ../$value/test/QC.fam.new
# argv[1]:pvalue
#opuput: ../$value/train.ped ../$value/train_ML.raw ../$value/test.ped ../$value/test_ML.raw
value=$1

#train
mv ../$value/train/QC.fam.new ../$value/train/QC_new.fam
mv ../$value/train/QC.bed ../$value/train/QC_new.bed
mv ../$value/train/QC.bim ../$value/train/QC_new.bim
/zfssz2/ST_MCHRI/BIGDATA/USER/jxs/prs_Tutorial/software/plink/plink \
    --bfile ../$value/train/QC_new \
    --recode \
    --out ../$value/train
 
/zfssz2/ST_MCHRI/BIGDATA/USER/jxs/prs_Tutorial/software/plink/plink \
    --bfile ../$value/train/QC_new \
    --recode A \
    --out ../$value/train_ML
   
#test
mv ../$value/test/QC.fam.new ../$value/test/QC_new.fam
mv ../$value/test/QC.bed ../$value/test/QC_new.bed
mv ../$value/test/QC.bim ../$value/test/QC_new.bim

/zfssz2/ST_MCHRI/BIGDATA/USER/jxs/prs_Tutorial/software/plink/plink \
    --bfile ../$value/test/QC_new \
    --recode \
    --out ../$value/test

/zfssz2/ST_MCHRI/BIGDATA/USER/jxs/prs_Tutorial/software/plink/plink \
    --bfile ../$value/test/QC_new \
    --recode A \
    --out ../$value/test_ML
