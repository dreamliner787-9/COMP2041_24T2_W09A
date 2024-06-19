#!/bin/dash

tutors=$(mlalias cs2041.24T2.tutors | grep -E '^\s*z' | sed 's/^\s*//')

all_courses=""

for zid in $tutors
do
	courses=$(acc $zid | grep -E '_Student' | cut -d':' -f2 | cut -d' ' -f2 | grep -E '^[A-Z]{4}[0-9]{4}t[123]' | cut -d'_' -f1 | sed -E 's/.{2}$//' | tr ' ' '\n')
	
	for course in $courses
	do
		all_courses="$all_courses$course"
	done
done
