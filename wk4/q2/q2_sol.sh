#!/bin/dash

# Solution 1
daytime=$(date)
time_of_day=$(echo "$daytime" | cut -d' ' -f5)
hour=$(echo "$time_of_day" | cut -d':' -f1)

if [ "$hour" -ge "9" ] && [ "$hour" -le "17" ]
then
	exit 0
else
	exit 1
fi

# Solution 2, less code, but harder to read :(
# current_hour="$(date "+%H")"
# test "$current_hour" -ge 9 -a "$current_hour" -lt 17
