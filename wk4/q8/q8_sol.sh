#!/bin/dash


tutors=$(mlalias cs2041.24T2.tutors | grep -E '^\s*z' | sed 's/^\s*//')
tutors_sep_by_space=$(echo "$tutors" | tr '\n' ' ')

all_courses=""

for zid in $tutors_sep_by_space
do
	their_courses=$(acc $zid | grep -E "[A-Z]{4}[0-9]{4}t._Student" | cut -d':' -f2 | cut -d' ' -f2 | cut -d'_' -f1 | sed -E 's/.{2}$//')
	
	all_courses="$all_courses\n$their_courses"
done

echo "$all_courses" | sort | sed -E '/^$/d'| uniq -c
