#!/bin/dash

for assignment in $(ls ~/cs3231);
do
	# Dont use the quote if you use the tilde ~ for home directory
	ln -s ~/cs3231/$assignment .
done
