#!/bin/dash

for file in $@
do	
	sed -E -i 's/COMP2041/COMP2042/g;s/COMP9044/COMP9042/g' $file
done
