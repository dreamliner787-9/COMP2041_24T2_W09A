#!/bin/dash

# next_commit_number=$(ls -1 .grip/master/commits | wc -l)

# mkdir .grip/master/commits/$next_commit_number

msg=$2
mkdir ".grip/master/commits/$msg"

for file in .grip/master/staging/*
do
    actual_filename=$(basename $file)
    if echo "$actual_filename" | grep -E "^\?" >/dev/null;
    then
        rm .grip/master/staging/"$actual_filename"
    else
        cp $actual_filename ".grip/master/commits/$msg/$actual_filename"
    fi
done