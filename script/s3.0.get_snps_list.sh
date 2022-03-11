#$1:fastGWA (../s2.gwas_train_result.fastGWA);$2: p_value (F: 1e-5)
# out: $pvalue/snp.list

input=$1
value=$2

if [ ! -d "../$value" ]; then
  mkdir ../$value
fi

if [ ! -d "../$value/train" ]; then
  mkdir ../$value/train
fi

if [ ! -d "../$value/test" ]; then
  mkdir ../$value/test
fi

awk -F '\t' '{if($13<=value){print $2}}' value="$value" ../s2.gwas_train_result.fastGWA >  ../"$value"/snp.list 