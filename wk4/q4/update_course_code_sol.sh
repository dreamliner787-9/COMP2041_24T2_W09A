#!/bin/dash

# $@ is all arguments separated by space.
for file in "$@"
do

	if [ ! -f "$file" ]; then
		continue
	fi
	
	sed -Ei 's/COMP2041/COMP2042/g;s/COMP9044/COMP9042/g' "$file"

done
