#!/bin/dash

all_paths=$(echo $PATH | tr ':' ' ')
program="$1"

for path in $all_paths
do
	if [ -f "$path/$program" ] 
	then
		ls -l "$path/$program"
		break
	fi
done
