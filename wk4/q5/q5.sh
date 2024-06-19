#!/bin/dash

echo $0
exit 0

for file in $@
do
	if [ -d "$file" ]
	then
		./$0 "$file"/*
	fi 
	
	if [ -f "$file" ]
	then
		sed -E -i 's/COMP2041/COMP2042/g;s/COMP9044/COMP9042/g' $file
	fi 
done
