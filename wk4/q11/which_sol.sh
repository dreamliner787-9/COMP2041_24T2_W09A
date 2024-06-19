#!/bin/dash

target="$1"
paths=$(echo "$PATH" | tr ':' ' ')

found=0
for path in $paths
do
	if [ -f "$path/$target" ]
	then
		ls -l "$path/$target"
	fi
done
