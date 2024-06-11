#!/bin/dash

for c_file in *.c
do
    echo "$c_file includes: "
    grep -E "^#" $c_file | 
    sed -E 's/^[^<"]*[<"]/    /' | # removes the first " or < and anything before it, then pad some spaces
    sed -E 's/[>"][>"]*$//' # removes the last " or < and anything after it

done