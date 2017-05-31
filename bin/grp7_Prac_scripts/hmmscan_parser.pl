# cat $1 | perl -e 
    while(<>)
    {
        if(/^\/\//)
        {
            $x=join("",@a);
            ($q)=($x=~/^Query:\s+(\S+)/m); # Grabs query name

            while($x=~/^>> (\S+.*?\n\n)/msg) # multiline, "." matches newline, global
            {
                $a=$&;
                @c=split(/\n/,$a);
                $c[0]=~s/>> //;
                for($i=3;$i<=$#c;$i++)
                {
                    @d=split(/\s+/,$c[$i]);
                    print $q."\t".$c[0]."\t$d[6]\t$d[7]\t$d[8]\t$d[10]\t$d[11]\n" if $d[6]<1;
                }
            }
            @a=();
        }
        else
        {
            push(@a,$_);
        }
    }

    #| sort -k 1,1 -k 6,6n -k 7,7n | uniq \| perl -e
    while(<>)
    {
        chomp;
        @a=split;
        next if $a[-1]==$a[-2];
        push(@{$b{$a[0]}},$_); # Removes lines with same start and end
    }

    foreach(sort keys %b) 
    {
            @a=@{$b{$_}};

            for($i = 0; $i < $#a; $i++) 
            {
                    @b = split(/\t/, $a[$i]);   # Alignment 1 = top alignment
                    @c = split(/\t/, $a[$i+1]); # Alignment 2 = bottom alignment
                    $len1 = $b[-1] - $b[-2]; # Length one = alignment 1 end - aligment 1 start
                    $len2 = $c[-1] - $c[-2]; # Length two = alignment 2 end - aligment 2 start
                    $len3 = $b[-1] - $c[-2]; # Length one = aligment 1 end - alignment 2 start

                    if($len3 > 0 and ($len3 / $len1 > 0.5 or $len3 / $len2 > 0.5)) # if alignments are overlaped and the overlap is greater than 50% the length of an alignment. 
                    {
                            if($b[2] < $c[2]) # Checks E value. Removes the alignment with the lowest Evalue.
                            {
                                    splice(@a, $i + 1, 1);
                            }
                            else
                            {
                                    splice(@a, $i, 1);
                            }
                            $i = $i - 1;
                    }
            }
            foreach(@a) 
            {
                    print $_ . "\n";
            }
    }

    # | uniq | perl -e 
    open(IN,"all.hmm.ps.len");
    while(<IN>)
    {
        chomp;
        @a=split;
        $b{$a[0]}=$a[1]; # creates hash of hmmName : hmmLength
    }

    while(<>)
    {
        chomp;
        @a=split;
        $r=($a[4]-$a[3])/$b{$a[1]}; # $a[4] = hmm end $a[3] = hmm start ; $b{$a[1]} = result of the hash of the name of the hmm (hmm length).
        print $_."\t".$r."\n";
    }

    # | perl -e 
    while(<>)
    {
        @a=split(/\t/,$_);
        if(($a[-2]-$a[-3])>80) # Good line!
        {
            print $_ if $a[2]<1e-5;
        }
        else
        {
            print $_ if $a[2]<1e-3;
        }
    }