# argv1: fastGWA_path  argv2: s2.P.stat.txt
@P = (1,0.1,0.01,0.001,0.0001,0.0001,0.00001,0.000001,0.0000001,0.00000001);
$train_fastGWA =$ARGV[0];
$out=$ARGV[1];
$out=join("", ">",$out);
open IN, $train_fastGWA;
$line = <IN>;
while ($line = <IN>) {
        chomp $line;
        @arr = split("\t",$line);
        foreach $item(@P){
                if($arr[0]<=22){
                        if($arr[12] <= $item){
                                $hash{$item} += 1;
                        }
                }
                
        }
}
close(IN);
open OUT,$out;
foreach $key(sort {$a<=>$b} keys %hash){
        print OUT $key."\t".$hash{$key}."\n";
}
close(OUT);

