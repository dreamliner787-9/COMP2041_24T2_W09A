#!/bin/dash

for assignment in $(ls ~/cs3231);
do

	ln -s ~/cs3231/$assignment .
done
