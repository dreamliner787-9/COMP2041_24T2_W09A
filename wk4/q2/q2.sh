#!/bin/dash

hour=$(date | cut -d' ' -f5 | cut -d':' -f1)

if [ $hour -ge 9 ] && [ $hour -le 17 ]
then
	exit 0
else
	exit 1
fi
